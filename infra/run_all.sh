
# infra/run_all.sh
#!/bin/bash
# Run all microservices + gateway

uvicorn api_gateway.main:app --reload --port 8000 &
uvicorn user_service.main:app --reload --port 8001 &
uvicorn job_service.main:app --reload --port 8002 &
