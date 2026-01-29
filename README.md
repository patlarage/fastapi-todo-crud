# FastAPI Todo CRUD API

A RESTful Todo API with full CRUD operations built with FastAPI.

## Features

- ✅ Create todos (POST)
- ✅ Get all todos (GET)
- ✅ Get single todo by ID (GET)
- ✅ Update todo (PUT)
- ✅ Delete todo (DELETE)
- ✅ Toggle complete status (PATCH)
- ✅ Pydantic validation (title length, required fields)
- ✅ Proper HTTP status codes (200, 201, 204, 404)
- ✅ 11 comprehensive tests (100% passing)

## Tech Stack

- **FastAPI** - Modern web framework
- **Pydantic** - Data validation
- **Uvicorn** - ASGI server
- **pytest** - Testing
- **httpx** - HTTP client for tests

## Installation
```bash
git clone https://github.com/jandaghi14/fastapi-todo-crud.git
cd fastapi-todo-crud
pip install -r requirements.txt
```

## Usage

Run the server:
```bash
uvicorn main:app --reload
```

API available at: http://127.0.0.1:8000

## API Endpoints

### Create Todo
```
POST /todos
Body: {"title": "Buy milk", "description": "From store"}
Response: 201 Created
```

### Get All Todos
```
GET /todos
Response: 200 OK
```

### Get Single Todo
```
GET /todos/{todo_id}
Response: 200 OK or 404 Not Found
```

### Update Todo
```
PUT /todos/{todo_id}
Body: {"title": "Updated", "description": "New description"}
Response: 200 OK or 404 Not Found
```

### Delete Todo
```
DELETE /todos/{todo_id}
Response: 204 No Content or 404 Not Found
```

### Toggle Complete
```
PATCH /todos/{todo_id}/complete
Response: 200 OK or 404 Not Found
```

## API Documentation

Interactive API docs:
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Testing

Run tests:
```bash
pytest test_main.py -v
```

All 11 tests passing ✅

## Project Structure
```
fastapi-todo-crud/
├── main.py              # API endpoints
├── models.py            # Pydantic models
├── test_main.py         # Test suite
├── requirements.txt     # Dependencies
├── .gitignore          # Git ignore
└── README.md           # Documentation
```

## What I Learned

- FastAPI CRUD operations
- HTTP status codes (201, 204, 404)
- HTTPException for error handling
- Path parameters and validation
- PUT vs PATCH differences
- In-memory data storage
- Testing FastAPI with TestClient
- Pydantic field validation with Field()

## Author

**Ali Jandaghi**
- GitHub: [@jandaghi14](https://github.com/jandaghi14)
- LinkedIn: [Ali Jandaghi](https://linkedin.com/in/ali-jandaghi-9a3188b1)
.idea/