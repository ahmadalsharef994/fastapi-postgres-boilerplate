# 🚀 FastAPI + PostgreSQL Boilerplate



## Overview
A production-ready boilerplate for building FastAPI applications with PostgreSQL integration, Docker support, and CI/CD via GitHub Actions.


This is a production-ready FastAPI + PostgreSQL boilerplate with:

- ✅ Dockerized setup
- ✅ GitHub Actions CI
- ✅ Modular folder structure
- ✅ PostgreSQL via Docker Compose


## Features
- Clean architecture with dependency injection
- PostgreSQL database integration
- Dockerized environment
- Automated testing with GitHub Actions


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


## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

Start building your next project faster 💡
