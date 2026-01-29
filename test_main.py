from fastapi.testclient import TestClient
from main import app, todos

client = TestClient(app)

# Helper to reset data between tests
def setup_function():
    todos.clear()

def test_create_todo():
    response = client.post("/todos", json={
        "title": "Test todo",
        "description": "Test description"
    })
    assert response.status_code == 201
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Test todo"
    assert response.json()["description"] == "Test description"
    assert response.json()["completed"] == False

def test_get_all_todos_empty():
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == []

def test_get_all_todos():
    # Create 2 todos first
    client.post("/todos", json={"title": "Todo 1", "description": "First"})
    client.post("/todos", json={"title": "Todo 2", "description": "Second"})
    
    # Get all
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["title"] == "Todo 1"
    assert response.json()[1]["title"] == "Todo 2"

def test_get_single_todo():
    # Create a todo first
    create_response = client.post("/todos", json={
        "title": "Single todo",
        "description": "Description"
    })
    todo_id = create_response.json()["id"]
    
    # Get it by ID
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id
    assert response.json()["title"] == "Single todo"

def test_get_single_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"

def test_update_todo():
    # Create a todo first
    create_response = client.post("/todos", json={
        "title": "Original title",
        "description": "Original description"
    })
    todo_id = create_response.json()["id"]
    
    # Update it
    response = client.put(f"/todos/{todo_id}", json={
        "title": "Updated title",
        "description": "Updated description"
    })
    assert response.status_code == 200
    assert response.json()["id"] == todo_id
    assert response.json()["title"] == "Updated title"
    assert response.json()["description"] == "Updated description"
    assert response.json()["completed"] == False  # Should not change

def test_update_todo_not_found():
    response = client.put("/todos/999", json={
        "title": "Updated",
        "description": "Test"
    })
    assert response.status_code == 404
    assert "Todo not found" in response.json()["detail"]

def test_delete_todo():
    # Create a todo first
    create_response = client.post("/todos", json={
        "title": "To be deleted",
        "description": ""
    })
    todo_id = create_response.json()["id"]
    
    # Delete it
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 204
    
    # Verify it's gone
    get_response = client.get(f"/todos/{todo_id}")
    assert get_response.status_code == 404

def test_delete_todo_not_found():
    response = client.delete("/todos/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"

def test_toggle_complete():
    # Create a todo first
    create_response = client.post("/todos", json={
        "title": "Toggle test",
        "description": ""
    })
    todo_id = create_response.json()["id"]
    
    # Toggle to complete
    response1 = client.patch(f"/todos/{todo_id}/complete")
    assert response1.status_code == 200
    assert response1.json()["completed"] == True
    
    # Toggle back to incomplete
    response2 = client.patch(f"/todos/{todo_id}/complete")
    assert response2.status_code == 200
    assert response2.json()["completed"] == False

def test_toggle_complete_not_found():
    response = client.patch("/todos/999/complete")
    assert response.status_code == 404
    assert response.json()["detail"] == "Todo not found"