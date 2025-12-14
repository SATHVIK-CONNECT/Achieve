from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser): 
    pass

class Quiz(models.Model):
    quizName = models.CharField(max_length=50)
    
    def __str__(self):
        return self.quizName
    
class Question(models.Model):
    quest = models.CharField(max_length=500)
    a = models.CharField(max_length=100)
    b = models.CharField(max_length=100)
    c = models.CharField(max_length=100)
    d = models.CharField(max_length=100)
    choice = models.CharField(max_length=100) 
    subject = models.ForeignKey(Quiz, on_delete=models.CASCADE, blank=True, null=True, related_name="topic")

    def __str__(self):
        return self.quest

class userQuiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    isActiveStatus = models.BooleanField(default=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user}'s {self.quiz}"