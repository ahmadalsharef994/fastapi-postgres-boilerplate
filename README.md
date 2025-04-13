# 🚀 SmartHub FastAPI + PostgreSQL Boilerplate

This is a production-ready FastAPI + PostgreSQL boilerplate with:

- ✅ Dockerized setup
- ✅ GitHub Actions CI
- ✅ Modular folder structure
- ✅ PostgreSQL via Docker Compose

### 🛠️ Tech Stack

- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker / Docker Compose
- GitHub Actions

### 🚀 Getting Started

1. Clone the repo  
2. Start Docker:

```bash
cd infra/docker
docker-compose up --build
```

3. Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

### 📂 Structure

```
app/
  ├── main.py
  ├── db/
  ├── routes/
  ├── models/
infra/
  └── docker/docker-compose.yml
```

Start building your next project faster 💡
