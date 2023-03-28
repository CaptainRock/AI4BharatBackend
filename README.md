# AI4BharatBackend
Backend Test From AI4Bharat

This project contains a Django web application that implements a simple translation service heler for Wikipedia articles. The application allows users to enter the name of a Wikipedia article and a target language, and then retrieves and displays a summary of the article along with a means to enter the translated sentences line by line.

Getting Started
To get started with this project, follow these steps:

Clone the repository to your local machine.
Install the project dependencies by running pip install wikipediaapi, nltk
Set up the database by running python manage.py migrate.
Run the development server by running python manage.py runserver.

The app is also hosted live at https://arupjyoti.pythonanywhere.com/

Frontend Tasks
The following frontend tasks were included in this coding exercise:

1.Implement a form that allows users to enter the name of a Wikipedia article and a target language.( The form is available at https://arupjyoti.pythonanywhere.com/) (Done)
2.Display all the sentences in the summary of the above Wikipedia article line by line along with individual textboxes to type the translations.(Done)
( Available when the Search button is clicked on the home page)
3.Display a dashboard to list all the projects in the DB. Clicking a project takes us to details of the project article as displayed in above task.
(Available at https://arupjyoti.pythonanywhere.com/dashboard)(Done)

Backend Tasks
The following backend tasks were included in this coding exercise:

1.Create a new entry in the project table to enter the details of Frontend task 1.(Done)
2.Using wikipedia api fetch the summary of the article from Frontend task 1. (Done)
3.Split the summary into sentences and store them in Sentence table and return all sentences to frontend (Done)
4.Update the sentences table after the translations have been entered. (Done)

Additional Notes
The project is configured to use a SQLite database by default.

