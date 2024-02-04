# Django Apps Repository

This repository contains a Django project with three apps - User Authentication, Recipes, and Student Report Card.

## Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
3. [Features](#features)
4. [Folder Structure](#folder-structure)
5. [License](#license)

## Introduction

This Django project serves as a foundation for building web applications with user authentication functionality. It includes three main apps:

- **User Authentication**: Provides user registration, login, and logout functionalities.
- **Recipes App**: Allows users to create, view, and manage recipes.
- **Student Report Card App**: Enables the creation and management of student report cards.

## Installation

### Prerequisites

- Python (>=3.6)
- Django (>=3.x)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your-repo
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for admin access:

    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:

    ```bash
    python manage.py runserver
    ```

7. Access the application at [http://localhost:8000](http://localhost:8000).

## Usage

- Access the Django admin interface at [http://localhost:8000/admin/](http://localhost:8000/admin/) using the superuser credentials created in the installation steps.
- Use the apps' functionalities as described in their respective sections.

## Features

### User Authentication

- User registration with email verification.
- User login and logout.
- Profile management.

### Recipes App

- Create, edit, and delete recipes.
- View a list of all recipes.
- Categorize recipes.
- Search functionality.

### Student Report Card App

- Add, edit, and delete student report cards.
- View a list of all report cards.
- Calculate and display overall grades.

## Folder Structure

- `user_authentication/`: User authentication app.
- `recipes/`: Recipes app.
- `student_report_card/`: Student Report Card app.
- `templates/`: HTML templates.
- `static/`: Static files (CSS, JavaScript, etc.).
- `manage.py`: Django management script.
- `README.md`: Project documentation.

## License

This project is licensed under the [MIT License](LICENSE).
