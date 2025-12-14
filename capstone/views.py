from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
from django.core.paginator import Paginator
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User, Quiz, Question, userQuiz
# Create your views here. 

def index(request):
    # cats = Category.objects.all()
    # levels = Level.objects.all()
    incompleted = []
    completed = [] 
    currentUser = request.user
    quizs = userQuiz.objects.all()
    for quiz in quizs:
        if quiz.user == currentUser:
            if quiz.isActiveStatus:
                incompleted.append(quiz)
            else:
                completed.append(quiz)
    
    return render(request, "capstone/index.html",{"completed":completed,"incompleted":incompleted}) 


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "capstone/login.html", {
                "note": "Invalid username and/or password."
            })
    else:
        return render(request, "capstone/login.html")
    

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, "capstone/register.html", {
                "note": "Passwords must match."
            })
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "capstone/register.html", {
                "note": "Username already taken."
            })
        login(request, user)
        
        quizs = Quiz.objects.all()
        for quiz in quizs:
            user_quiz = userQuiz(user=request.user, quiz=quiz)
            user_quiz.save()

        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "capstone/register.html")
    
def profile(request):
    currentUser = request.user
    usersquiz = userQuiz.objects.all()
    count = 0
    incompleteCount = 0
    for user in usersquiz:
        if user.user == currentUser:
            if user.isActiveStatus:
                incompleteCount += 1
            else: 
                count += 1

    return render(request, "capstone/profile.html",{"count":count, "incomplete":incompleteCount})

def quiz(request, id):
    quiz = Quiz.objects.get(pk=id)
    questions = Question.objects.filter(subject=quiz).order_by('id').reverse()
    usersquiz = userQuiz.objects.get(user=request.user, quiz=quiz.id)
    paginator = Paginator(questions, 1)
    page_no = request.GET.get('page')
    potp = paginator.get_page(page_no)

    return render(request, 'capstone/quiz.html',{"potp":potp,"usersquiz":quiz,"quiz":usersquiz})

def correction(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        # quiz = Quiz.objects.get(pk=id)
        # currentUser = request.user
        user_quiz = userQuiz.objects.get(pk=id)
        user_quiz.score = data['score']
        user_quiz.save()
        return JsonResponse({"note":"Score incremented", "data":data['score']})
    
@csrf_exempt
def submission(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        # quiz = userQuiz.objects.get(pk=id)
        # currentUser = request.user
        user_quiz = userQuiz.objects.get(pk=id)
        user_quiz.isActiveStatus = False
        user_quiz.score = data['score']
        user_quiz.save()
        return JsonResponse({"note":"Submitted", "data":data['score']})

def scores(request):
    currentUser = request.user
    quizzes = userQuiz.objects.all()
    quizs = []
    for quiz in quizzes:
        if quiz.user == currentUser:
            if not quiz.isActiveStatus:
                quizs.append(quiz)

    return render(request, 'capstone/scores.html',{"quizs":quizs, "user":currentUser})

def adminUi(request):
    quizs = Quiz.objects.all()
    return render(request, "capstone/adminUi.html",{"categories":quizs})

def addQuiz(request):
    if request.method == "POST":
        quiz = request.POST['quiz']
        newQuiz = Quiz(quizName = quiz)
        newQuiz.save()

        users = User.objects.all()
        for user in users:
            userQuiz(user=user, quiz=newQuiz).save()

    return HttpResponseRedirect(reverse(index))

def addQuestion(request):
    if request.method == "POST":
        quest = request.POST['quest']
        optA = request.POST['optA']
        optB = request.POST['optB']
        optC = request.POST['optC']
        optD = request.POST['optD']
        choice = request.POST['choice']
        category = request.POST['category']

        categoryData = Quiz.objects.get(quizName = category)

        newQuestion = Question(quest = quest, a = optA, b = optB, c = optC, d = optD, choice = choice, subject = categoryData)
        newQuestion.save()
    return HttpResponseRedirect(reverse(index))
