# 🔄 Django URL Health Checker (Celery + Redis)

This project is a Django-based web application that allows users to submit URLs and automatically checks their health (up/down status and response time) periodically using Celery and Redis.

## 🔧 Features

- Submit URLs via API
- Background health checks using Celery
- Redis as message broker
- Celery Beat for periodic scheduling (every 5 minutes)
- Store response time and status
- REST API to view last 5 health check results
- Admin panel for managing URLs
- Bonus: Setup-ready for alerting via email or logs

## 🚀 Tech Stack

- Django
- Celery
- Redis
- Django REST Framework
- Django Celery Beat
- PostgreSQL / SQLite (by default)
- CORS headers

## 📦 Setup Instructions

```bash
# Clone repo and move into it
git clone https://github.com/your-username/urlchecker.git
cd urlchecker

# Create and activate virtualenv
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Migrate and run
python manage.py migrate
python manage.py runserver
