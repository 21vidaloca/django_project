# Django Web Application

##  Overview
A full-stack web application built with Python and the Django framework. This project demonstrates backend routing, server-side rendering, and relational database management. 

*(Note: Add 1-2 sentences here explaining exactly what the app does. E.g., "This application allows users to register, log in, and manage personal tasks.")*

##  Features
* **Backend:** RESTful routing and data handling using Django.
* **Frontend:** Dynamic, responsive UI built with HTML, CSS, and Django Templates.
* **Database Management:** Integrated SQL database with automated backup and restoration scripts (`backup.bat` and `fisier.sql`).
* **Error Handling:** Custom error logging and tracking (`erori.txt`).

##  Tech Stack
* **Language:** Python
* **Framework:** Django
* **Frontend:** HTML5, CSS3
* **Database:** SQLite / PostgreSQL *(Change this to whichever you used)*

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/21vidaloca/django_project.git](https://github.com/21vidaloca/django_project.git)
   cd django_project
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
