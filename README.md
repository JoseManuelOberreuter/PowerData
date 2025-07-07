# Health Check Service

## User Stories
As a system user, I want to query the `/health` endpoint that returns the microservice's status, so that I can automatically monitor its health in development environments.

## Architecture

The service follows a scaffold clean architecture pattern with the following structure:

[![Open Architecture Diagram in Figma](https://img.shields.io/badge/Figma-Architecture_Diagram-blue?style=for-the-badge&logo=figma)](https://www.figma.com/board/j8ANmrkNFXwcEwTCL3FxA5/PowerData?node-id=0-1&t=BAvtii6EBYMoHIeB-1)


## Directory Tree

```
health_check_service/
├── main.py
├── requirements.txt
├── app/
│   ├── infrastructure/
│   │   ├── api/
│   │   │   └── health_router.py
│   │   └── repository/
│   │       └── health_repository.py
│   ├── domain/
│   │   ├── use_cases/
│   │   │   └── health_check_usecase.py
│   │   └── models/
│   │       └── health_status.py
│   └── config/
│       └── settings.py
└── tests/
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