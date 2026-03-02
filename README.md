# Django Web Application

##  Overview
Developed a full-stack e-commerce application in Django featuring a custom user authentication system with UUID-based email verification and IP-tracking to prevent brute-force login attacks.

Engineered a relational database (Django ORM) for products and categories, implementing an advanced search engine with multi-parameter filtering, custom form validation, and pagination.

Implemented Role-Based Access Control (RBAC) for administrative routes and built a custom server-side traffic logging and analytics system to monitor user activity.


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
