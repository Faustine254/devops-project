# Task Manager — Production DevOps Project

A production-ready web application built to demonstrate a full DevOps workflow.
Built with Python/Flask + PostgreSQL, served via Nginx, fully containerised with Docker.

---

## Live Architecture
Browser → Nginx (port 80) → Flask/Gunicorn (port 5000) → PostgreSQL (port 5432)

All services run in Docker containers orchestrated by Docker Compose.

---

## Tech Stack

| Layer     | Technology              |
|-----------|-------------------------|
| App       | Python 3.12, Flask      |
| WSGI      | Gunicorn                |
| Database  | PostgreSQL 16           |
| Proxy     | Nginx                   |
| Container | Docker + Docker Compose |
| CI/CD     | GitHub Actions (Step 2) |
| Cloud     | AWS EC2 (Step 3)        |

---

## Run Locally

### Prerequisites
- Docker
- Docker Compose

### Start the app

```bash
git clone https://github.com/YOUR_USERNAME/devops-project.git
cd devops-project
docker compose up --build
```

Visit **http://localhost**

---

## API Endpoints

| Method | Endpoint            | Description     |
|--------|---------------------|-----------------|
| GET    | `/health`           | Health check    |
| GET    | `/api/tasks`        | List all tasks  |
| POST   | `/api/tasks`        | Create a task   |
| PUT    | `/api/tasks/<id>`   | Update a task   |
| DELETE | `/api/tasks/<id>`   | Delete a task   |

### Example

```bash
# Health check
curl http://localhost/health

# Create a task
curl -X POST http://localhost/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Learn DevOps", "description": "Docker, CI/CD, AWS"}'

# List tasks
curl http://localhost/api/tasks
```

---

## Project Structure
devops-project/
├── app/
│   ├── wsgi.py            # Flask application + API routes
│   ├── requirements.txt   # Python dependencies
│   ├── Dockerfile         # Container image
│   └── templates/
│       └── index.html     # Frontend UI
├── nginx/
│   ├── nginx.conf         # Nginx main config
│   └── conf.d/
│       └── app.conf       # Reverse proxy config
├── docker-compose.yml     # Orchestrates all services
└── README.md

---

## What This Project Demonstrates

- Containerising a Python web app with Docker
- Multi-service orchestration with Docker Compose
- PostgreSQL with persistent named volumes
- Nginx as a reverse proxy with security headers
- Health checks and service dependency ordering
- Production WSGI server (Gunicorn)
