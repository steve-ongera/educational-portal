# 🎓 Django Educational Portal

## 📘 Project Overview

This Django-based Educational Portal is a comprehensive web application designed to facilitate interactions between students and teachers, providing features for course registration, assignment submission, and academic management.

## 🚀 Features

### Authentication
- User registration (Student and Teacher roles)
- Secure login system
- Role-based dashboard access
- Logout functionality

### Student Features
- Unit registration
- Assignment submission
- View registered units
- Session reporting
- Personal dashboard

### Teacher Features
- Create and post assignments
- View student submissions
- Manage teaching units
- Personalized dashboard

## 🔧 Prerequisites

- Python 3.8+
- Django 3.2+
- pip (Python package manager)

## 🛠 Project Structure

```
educational_portal/
│
├── accounts/
│   ├── views.py
│   ├── models.py
│   ├── forms.py
│   └── urls.py
│
├── portal/
│   ├── views.py
│   ├── models.py
│   ├── templates/
│   │   ├── auth/
│   │   └── portal/
│   └── urls.py
│
├── manage.py
└── requirements.txt
```

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/steve-ongera/educational-portal.git
   cd educational-portal
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Database setup:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

## 🔐 Authentication Workflow

### User Registration
- Separate registration for students and teachers
- Validation checks for:
  - Password matching
  - Unique username
  - Unique email
- Role assignment (student/teacher)

### Login Process
- Authenticate user credentials
- Redirect to appropriate dashboard based on role
  - Students → Student Dashboard
  - Teachers → Teacher Dashboard

### Authorization
- `@login_required` decorator ensures protected views
- Role-based access control

## 📋 Key Views and Functionalities

### Student Views
- `register_units()`: Register for academic units
- `submit_assignment()`: Submit assignments
- `student_dashboard()`: View personal academic information
- `report_session()`: Report academic sessions

### Teacher Views
- `students_in_unit()`: View students in a specific unit
- `view_submissions()`: Review student assignment submissions
- `teacher_dashboard()`: Manage teaching units
- `post_assignment()`: Create and post new assignments

## 📝 Configuration

### settings.py Recommendations
```python
INSTALLED_APPS = [
    'accounts',
    'portal',
    # ... other apps
]

AUTH_USER_MODEL = 'accounts.CustomUser'  # If using custom user model

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
```

## 🧪 Testing

Run tests:
```bash
python manage.py test accounts
python manage.py test portal
```

## 🔒 Security Features
- Password hashing
- CSRF protection
- Role-based access control
- File upload validation
- Secure authentication mechanisms

## 🚧 Deployment Checklist
1. Set `DEBUG = False`
2. Configure static files
3. Set up production database
4. Use environment variables for sensitive information
5. Configure ALLOWED_HOSTS
6. Set up HTTPS

## 📚 Additional Resources
- [Django Documentation](https://docs.djangoproject.com/)
- [Django Authentication System](https://docs.djangoproject.com/en/stable/topics/auth/)

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## 📄 License
[MIT]

## 🛎️ Support
For issues or questions, please open a GitHub issue.

---

**Pro Tip:** Always keep your dependencies updated and follow Django's security best practices!