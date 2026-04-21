# 🌤️ Weather Locations REST API

> A Django REST Framework API for managing geographic locations with CRUD functionality and JSON Web Token - JWT authentication.

[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=flat\&logo=django\&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat\&logo=python\&logoColor=white)](https://www.python.org/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.14+-A435F0?style=flat\&logo=django\&logoColor=white)](https://www.django-rest-framework.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 Overview

This project is a **REST API** built with Django REST Framework that provides CRUD operations for geographic locations. Each location includes a name, latitude, and longitude.

All API endpoints require authentication via JWT tokens.

---

## 🎯 Features

* CRUD operations for weather locations
* RESTful endpoints with hyperlinked serialization
* JWT authentication (SimpleJWT)
* Session authentication (for Django admin)
* Input validation for coordinates
* Django admin integration
* Environment-based configuration (`.env`)
* SQLite database (default)

---

## 🛠️ Tech Stack

| Layer     | Technology            |
| --------- | --------------------- |
| Framework | Django 6.0              |
| API       | Django REST Framework   |
| Language  | Python 3.10+            |
| Database  | SQLite                  |
| Auth      | JWT + Session           |

---

## 🚀 Quick Start

### Prerequisites

* Python 3.10+
* pip

### Installation

```bash
git clone https://github.com/daenalan/drf-weather-locations.git
cd drf-weather-locations

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
```

### Setup

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint              | Description          |
| ------ | --------------------- | -------------------- |
| POST   | `/api/token/`         | Obtain JWT token     |
| POST   | `/api/token/refresh/` | Refresh JWT token    |

### Locations

| Method | Endpoint              | Description           |
| ------ | --------------------- | --------------------- |
| GET    | `/api/v1/`            | List all locations    |
| POST   | `/api/v1/`            | Create a location     |
| GET    | `/api/v1/{id}/`       | Retrieve a location   |
| PUT    | `/api/v1/{id}/`       | Update a location     |
| PATCH  | `/api/v1/{id}/`       | Partial update        |
| DELETE | `/api/v1/{id}/`       | Delete a location     |

> **Note:** All location endpoints require a valid JWT token in the `Authorization` header: `Authorization: Bearer <token>`

### Example Usage

```bash
# Obtain token
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'

# List locations (with token)
curl http://localhost:8000/api/v1/ \
  -H "Authorization: Bearer <your-token>"
```

---

## 📁 Project Structure

```
drf-weather-locations/
├── core/
│   ├── settings.py      # Django settings
│   ├── urls.py          # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── locations_api/
│   ├── models.py        # WeatherLocation model
│   ├── views.py         # ViewSet with auth
│   ├── serializers.py   # Hyperlinked serializer
│   ├── urls.py          # API routes (v1)
│   └── admin.py         # Admin configuration
├── .env                 # Environment variables
├── manage.py
├── requirements.txt
└── README.md
```

---

## 💡 What This Project Demonstrates

* Django 6.0 + DRF setup
* ModelViewSet with authentication
* HyperlinkedModelSerializer
* JWT authentication (SimpleJWT)
* Session authentication

---

## 🔮 Possible Improvements

* Add filtering and pagination
* Use MySQL/PostgreSQL
* Docker setup
* Add more validation

---

## 📄 License

MIT License

---

## 👤 Author (@daenalan)

Built with Django REST Framework

---