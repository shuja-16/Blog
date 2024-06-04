# Blog Web App

This is a simple blog web application built using the Django framework. It includes basic authentication features such as user login, and logout.

## Features

- User login and logout
- Create, read, update, and delete blog posts
- List all blog posts
- View individual blog posts
- Basic user authentication

## Requirements

- Python 3.x
- Django 3.x or later
- SQLite (default database for Django)

- 3. **Install the required packages:**
    ```sh
    pip install django djangorestframework environ djangorestframework-simplejwt
    ```

4. **Apply migrations:**
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser (admin account):**
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7. **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`.
