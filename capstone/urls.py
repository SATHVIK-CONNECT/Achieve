from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout'),
    path('adminUi', views.adminUi, name= 'adminUi'),
    path('profile', views.profile, name='profile'),
    path('quiz/<int:id>', views.quiz, name='quiz'),
    path('correction/<int:id>', views.correction, name='correction'),
    path('submission/<int:id>', views.submission, name='submission'),
    path('scores', views.scores, name='scores'),
    path('addQuiz', views.addQuiz, name='addQuiz'),
    path('addQuestion', views.addQuestion, name='addQuestion')
]