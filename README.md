# Health Check Service

## User Stories
As a system user, I want to query the `/health` endpoint that returns the microservice's status, so that I can automatically monitor its health in development environments.

## Architecture

The service follows a scaffold clean architecture pattern with the following structure:

[![Open Architecture Diagram in Figma](https://img.shields.io/badge/Figma-Architecture_Diagram-blue?style=for-the-badge&logo=figma)](https://www.figma.com/board/j8ANmrkNFXwcEwTCL3FxA5/PowerData?node-id=0-1&t=BAvtii6EBYMoHIeB-1)


## Directory Tree

```
health-check-service/
├── main.py
├── requirements.txt
├── Dockerfile
├── README.md
├── app/
│   ├── __init__.py
│   ├── config/
│   │   └── settings.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── models/
│   │   │   └── health_status.py
│   │   └── use_cases/
│   │       └── health_check_usecase.py
│   └── infrastructure/
│       ├── __init__.py
│       └── api/
│           └── health_router.py
├── deployment/
│   ├── deploy.sh
│   └── docker-compose.yml
└── tests/
    ├── __init__.py
    └── test_health.py

```

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the application
```bash
python main.py
```

Or with uvicorn directly:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Test the endpoint
```bash
curl http://localhost:8000/api/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00.123456",
  "message": "Service is running normally"
}
```

### 4. Run tests
```bash
pytest tests/
```

### 5. API Documentation (Swagger)
```bash
http://localhost:8000/docs
```

## Functional Documentation

### Business Rules
- Health check always returns "healthy" status
- Includes timestamp and service message
- No authentication required

### Use Cases
- **UC001**: Get service health status
  - **Input**: HTTP GET request to `/api/health`
  - **Output**: JSON with status, timestamp, and message

## Technical Documentation

### Technology Stack
- **Framework**: FastAPI
- **Language**: Python 3.11
- **Server**: Uvicorn
- **Architecture**: Clean Architecture
- **Testing**: Pytest
- **Containerization**: Docker

### Configuration
- **Port**: 8000
- **Environment**: Development
- **Settings**: `app/config/settings.py`

## Quality Documentation

### Test Coverage
- **Unit Tests**: Domain models and use cases
- **Integration Tests**: API endpoints
- **Test Runner**: `pytest tests/`

### Code Quality
- **Architecture**: Clean Architecture pattern
- **Separation of Concerns**: Domain, Infrastructure, Config
- **Error Handling**: Built-in FastAPI error handling