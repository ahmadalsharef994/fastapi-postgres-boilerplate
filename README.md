docker compose -f infra/docker/docker-compose.yml up --build
# 🚀 SmartHub Boilerplate

**SmartHub** is a modular, real-world boilerplate for building scalable backend systems using **FastAPI**, **PostgreSQL**, **microservices**, **Docker**, and **Airflow**.  
It’s built with best practices in mind, so any developer can plug in their own business logic and get started fast.

---

## 🧠 Why SmartHub?

This project is a **production-ready template** that helps you:

- Build scalable, event-driven microservices
- Use FastAPI with SQLAlchemy and PostgreSQL per service
- Leverage Docker Compose for local dev
- Add ETL/ELT pipelines via Airflow
- Expose Prometheus metrics for observability
- Enable WebSockets for real-time features
- Implement JWT auth and RBAC
- Use GitHub Actions for CI/CD

Whether you're building an HR platform, job board, marketplace, or AI service backend — this boilerplate gives you a strong, modular starting point.

---

## 📦 Microservices

| Service         | Description                                      |
|-----------------|--------------------------------------------------|
| `api_gateway`   | Central entrypoint, auth, routing, WebSockets    |
| `user_service`  | User CRUD, auth, roles                           |
| `job_service`   | Job CRUD, filters                                |
| `ai_service`    | Resume parsing and job matching (NLP-ready)      |

---

## 🛠️ Tech Stack

- **FastAPI** (sync) + **SQLAlchemy**
- **PostgreSQL** per microservice
- **Docker** + **Docker Compose**
- **Apache Airflow** for scheduled data pipelines
- **Prometheus** for monitoring (`/metrics`)
- **WebSockets** for real-time notifications
- **Internal Event Bus** (pub/sub microservices)
- **GitHub Actions** for CI/CD

---

## 🧰 Project Structure

```
SmartHub/
├── api_gateway/
│   ├── main.py, database.py, Dockerfile
│   ├── auth/, events/, middlewares/, routes/
├── user_service/
│   ├── main.py, db.py, Dockerfile
│   ├── auth/, models/, routes/
├── job_service/
│   ├── main.py, db.py, Dockerfile
│   ├── models/, routes/
├── ai_service/
│   ├── main.py, Dockerfile
│   ├── resume_parser.py, matcher.py
├── infra/
│   ├── docker/docker-compose.yml
│   ├── airflow/dags/etl_pipeline.py (+ Dockerfile)
│   └── prometheus/prometheus.yml
├── .github/workflows/ci.yml
├── .env, README.md, run_all.sh
```

---

## ✅ Features Implemented

- 🔐 JWT auth with login/register
- 👥 Role-based access control (RBAC)
- 📄 User + Job CRUD
- 📄 Resume parsing + job matching logic
- 📊 Prometheus metrics with `prometheus-fastapi-instrumentator`
- 🔁 Real-time WebSocket messaging
- 🛠️ GitHub CI/CD pipeline
- ⏱️ Airflow DAG for scheduled ETL

---

## 🚀 Getting Started

1. **Clone the repo**

```bash
git clone https://github.com/your-username/smarthub.git
cd smarthub
```

2. **Start all services**

```bash
cd infra/docker
docker-compose up --build
```

3. **Access services**

| Service        | URL                        |
|----------------|----------------------------|
| API Gateway    | http://localhost:8000      |
| Airflow        | http://localhost:8080      |
| Prometheus     | http://localhost:9090      |

> Use the `.env` file to configure credentials and ports.

---

## 💡 How to Extend

You can add more microservices (e.g., payment, notifications), extend the AI logic, or plug in a frontend (`React`, `Tailwind`, etc.) by building on top of this foundation.

---

## 📄 License

MIT — free to use and modify. Give credit if helpful!

---

## 👨‍💻 Author

Built by **Ahmad**, PhD in AI and Senior Software Engineer with 9+ years experience.  
Let’s connect on [LinkedIn](https://www.linkedin.com) or [GitHub](https://github.com)!

---
