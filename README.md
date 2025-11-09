# BLOG-WEB-APPLICATION-USING-DJANGO

**A Modern Community-Driven Blogging Platform**

![Python](https://img.shields.io/badge/Python-100.0%25-blue)
![Last Commit](https://img.shields.io/badge/last%20commit-today-brightgreen)

Built with the tools and technologies:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

---

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Testing](#testing)

---

## Overview

**Blog-Web-Application-using-Django** is a full-stack web application built with Django that enables users to create, share, and explore blog posts within a collaborative community. The application provides a seamless blogging experience with user authentication, content management, and interactive features for community engagement.

### Why Blog-Web-Application-using-Django?

This project demonstrates modern web development practices and showcases key Django capabilities for building scalable web applications. The core features include:

- 👥 **Community Hub**: Connect with other bloggers and readers in an interactive environment.
- ✍️ **Content Creation**: Write, edit, and publish blog posts with rich formatting capabilities.
- 🔐 **User Authentication**: Secure user registration, login, and profile management.
- 💬 **Engagement**: Comment, like, and interact with posts from the community.
- 🏷️ **Categorization**: Organize posts by topics and tags for easy discovery.
- 🎯 **Responsive Design**: Works seamlessly across all devices and screen sizes.

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language**: Python (3.8 or higher)
- **Framework**: Django (3.2+)
- **Database**: SQLite (default)
- **Package Manager**: pip or Conda

### Installation

Build Blog-Web-Application-using-Django from the source and install dependencies:

1. **Clone the repository:**

```bash
git clone https://github.com/JayeshSPatel/Blog-Web-Application-using-Django
cd Blog-Web-Application-using-Django/Blog\ Application\ Using\ Django/studybud
```

2. **Create a virtual environment:**

Using venv:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Using conda:

```bash
conda create -n studybud python=3.9
conda activate studybud
```

3. **Install the dependencies:**

Using pip:

```bash
pip install -r requirements.txt
```

Using conda:

```bash
conda install --file requirements.txt
```

4. **Apply migrations:**

```bash
python manage.py migrate
```

5. **Create a superuser (optional):**

```bash
python manage.py createsuperuser
```

---

## Project Structure

```
studybud/
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── db.sqlite3               # SQLite database
├── studybud/                # Main project directory
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── base/                    # Main app directory
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL routes
│   ├── forms.py             # Django forms
│   ├── admin.py             # Admin panel configuration
│   └── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── home.html        # Home page
│       ├── room.html        # Room/Post detail page
│       └── ...
└── static/                  # Static files (CSS, JS, images)
```

---

## Usage

### Running the Development Server

Start the Django development server:

Using pip:

```bash
python manage.py runserver
```

Using conda:

```bash
conda activate studybud
python manage.py runserver
```

The application will be accessible at `http://127.0.0.1:8000/`

### Accessing the Admin Panel

Open your browser and navigate to:

```
http://127.0.0.1:8000/admin/
```

Log in with your superuser credentials to manage posts, users, and site content.

---

## Testing

Run the test suite with:

Using pip:

```bash
python manage.py test
```

Using conda:

```bash
conda activate studybud
python manage.py test
```

---

⬆ [Return to Top](#blog-web-application-using-django)
