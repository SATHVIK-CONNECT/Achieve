# Sharp

#### Video Demo: https://youtu.be/B1jjdqquivI?si=wQ8q6wW-3eBW6GWp

#### Description:

Welcome to Sharp!

This is my Final Project for the course CS50’s Introduction to Computer Science. It is developed by JavaScript and Python.

## What is Sharp?

This quiz application is like a tool for testing knowledge. It's a comprehensive learning platform designed to engage users, track progress.

This project is a web application that allows users to Practice & improve their skills with Multiple Choice Questions.

This document provides a detailed overview of the app's functionality, and project structure.

## Features of the Project

- **Dynamic Result Analysis**: This project dynamically stores the Current Quiz Progress as Score and displays it on the Quiz Session. Once the Quiz is submitted, the site shows the Result for the overall Quiz.

- **Achievements**: Achivements for the completed Quizzes. This can be particularly beneficial for classroom settings or encouraging friendly competition among learners.

- **Alerts or Warnings**: It provides alerts for the Sessions. It actually used JavaScript mechanism to Prevent the Reloading of the webpage by sending an alert to the user to warn about results. And also prevents the navigation to back page.

- **User-Friendly Interface**: The app prioritizes a clean and intuitive user interface that facilitates seamless quiz-taking. There is no complex interfaces in this project that user cannot understand. This enhances user experience and accessibility for learners of all backgrounds.The user can see the score after completing the Quiz.

- **Customization**: The project is designed with modularity in mind. New Quizzes and Questions can be easily creatable for admin by Admin User Interface. Specially designed for admin to Add Quizzes.

- **Multi User Capability**: The Multi User Capability means that the project having multi user interface. The project allows multiple users access and each user login takes up to their respective interface. Each user gets their quizzez as per their quiz data.

- **Admin Interface**: Admin Interface means that having an interface specially for the admin. For the Admin to create the Quizzes and questions. It is added in index with a condition, so the admin of this app can only view the Admin Interface.

- **Mobile Responsive**: Mobile responsive means that the project can be supported or get the accurate design in mobile also. This capstone project can achieves this factor.

- **Fetch Call**: Fetch call means that fetching data from database without page reload. This capstone project consists of 2 fetch calls correction and submission. One is for correcting the question and giving score respectively. Another one is for submitting the quiz and making the quiz inactive for that user.

- **Pagination**: Pagination allows us to go through pages in a single interface. This project having pagination for questions to be appeared a single question in page.

- **Js Pre-defined Functions**: This project having some pre-defined JavaScript Operations. They are preventBack and preventReload.
  - PreventReload means that preventing the page reload for user confirmation and to not let the user to cheat.
  - PreventBack means that preventing the back page, So user cannot move back in the Quiz.

The above functionalities making the Capstone project complex than the other projects.

## Project File Breakdown:

### Static Files

- **scripts.js**: This file contains the JavaScript code for the quiz functionality, including the logic for displaying the quiz questions, storing the user's answers, and calculating the score. And fetching the data from django database for updating the score dynamically. It consists of 3 functions. They are getCookie(), correction(), submission().
- **styles.js**: This file consists of aesthetics for the HTML elements by targeting elements by their class name or Id or Tag name. This file specifies the overall look and feel of the django project Sharp.

### Templates

- **adminUi.html**: This is the admin interface for adding new quizzes and questions for the particular quiz. It contains a form that takes input from the admin and stores the values in tables of database.

- **index.html**: This is the main page of the project. It contains a quizzes as well as the login, register links. It works by a condition, if user is authenticated it shows the quizzes or else it shows the links navigating to Login Page and Register Page.

- **layout.html**: This is the base template for all the pages in the project. It contains

  - Navigation bar
    In here, We actually have 3 Links. They are Sharp(Index Page), Scores and Profile.

  - Footer
    It is specifically designed for the Admin to navigate to an interface of admin named adminUi.html. It shows a Link if the user is superuser/Admin/First User of the Project.

- **login.html**: This is the login page of the project. It takes the username and password to the database and compares with the existed data and returns as per the return value. If user is not in login details then the site will be get back to the Login/Register Page itself. similarly with the Register form. It takes user to index if the credentials of the forms are accurate.

- **profile.html**: This is the profile page of the user. It shows the user's details like displaying the count of completed quizzes and incomplete quizzes for the current user and an option to Log out the Website.

- **quiz.html**: This is the quiz page of the project. It contains of the questions that are belongs to the quiz with multiple choices. And a score element at the top-right corner, which counts the correct answer count for the quiz and displays it. It also shows Result after submitting the quiz. It uses the pagination for question to be appeared separately.

- **register.html**: This is the register page of the project. It takes the username, email and password with confirmation. And compares with credentials in database. Creates new user based on the return value of the condition.

- **scores.html**: This is the scores page of the project. It displays the scores of the projects. It actually designed as Achievements, to show the completed quizzes of the user as an Achievement, and if we click on that quiz then it takes the user to Result of the Quiz.

### Django Files

- **models.py**: Contains the definition of models for quizzes, questions, answer choices, and scores

- **admin.py**: Contains the admin interface for managing quizzes, questions, and scores

- **apps.py**: Contains the configuration for the Sharp app

- **tests.py**: Contains unit tests for the Sharp app

- **urls.py**: Contains the URL configuration for the Sharp app

- **views.py**: Handles user interaction by implementing logic for displaying quizzes, processing user responses, calculating scores, and generating feedback.

- **requirements.txt**: Lists all necessary Python packages required for project functionality.

- **settings.py**: This file contains project-wide configuration settings. It includes database configuration, installed apps, template directories, static file directories, and other essential settings for your project.

- **wsgi.py**: This file is an entry point for WSGI-compatible web servers to serve your project.

- **manage.py**: This file is the command-line utility that lets you interact with your Django project. You use it to perform various tasks like running the development server, creating superusers, migrating the database, and more.

## Running the Application:

To run the Quiz App, follow these steps:

- **Clone the repository**: Obtain the project code from the repository.
- **Create a virtual environment**: Set up a virtual environment to isolate project dependencies.
- **Install requirements**: Install necessary packages using pip install -r requirements.txt.
- **Database configuration**: Configure database settings in settings.py.
- **Database migration**: Run python manage.py migrate to create database tables.
- **Start development server**: Run python manage.py runserver to start the application.

## Additional Information:

### How to use?

- Go to this Capstone URL. It will take you to Index Page of this Capstone project consisting of two links Login and Register.
- Login page takes you to signin page of the Capstone Project. You need to fill the user name and password to go to Main page.
- Register Page takes you to Register page. You need to fill the required fields to open a account in this Quiz app. And then it takes you to Main page.
- After Login or Register, You will go to The Main Page, it is also the Index page which is differentiated by a condition based on user authentication. It consists of a header which contains Title, Scores, Profile and It shows you the Multiple Quizzes which are currently active in this Quiz App.
- Title is Title of the Quiz App(Sharp). If you click on it, it takes you to Main Page if you're in another page.
- Scores link shows you completed quizzes as an Achievements.
- Profile link shows you How many quizzes you completed and How many are left and a Logout link.
- In the Main page with quizzes, you will be able to take the quiz if you click the Quiz's attempt option. And then it takes you to Quiz with questions. After submitting the quiz, you will see the Result. Then this quiz will be Categorized as completed quiz in the main page and you will get an achievement.
- Quiz Page consists of Title of the Quiz, question and options to select. You need to click on any option and then click next to see the next question. If your option is correct, you're score will be incremented else not. In the last question, you will see a Submit button instead of next, this button can submit the quiz.
- Logout link let's you logout of the Quiz app and takes you to Index with Login and Register links.

This project utilizes the Django framework, leveraging its built-in functionalities for user authentication, database management, and security measures.
For deployment, consider using platforms like Heroku or AWS to make the application accessible online.

By combining user-friendly features, advanced functionalities, and a robust Django backend. With its modular design and potential for customization, it can be tailored to various educational or self-assessment needs

## Conclusion:

This README.md file provides a detailed overview of the Capstone Project - Quiz App. By this, you will know

- What is the project?
- File Structure.
- How to run it and use it?
