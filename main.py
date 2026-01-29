from fastapi import FastAPI, HTTPException
from models import Todo, TodoCreate
from typing import List

app= FastAPI()

todos: list[Todo]= []
next_id= 1

def get_todo_by_id(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return None

@app.post('/todos', status_code=201)
def create_todo(todo: TodoCreate) -> Todo:
    global next_id
    
    new_todo= Todo(id= next_id,
                   title=todo.title,
                   description= todo.description,
                   completed=False
                   )
    todos.append(new_todo)
    next_id+=1
    return new_todo

@app.get('/todos')
def get_all_todos() -> list[Todo]:
    return todos 

@app.get('/todos/{todo_id}')
def get_single_todo(todo_id:int) -> Todo:
    todo= get_todo_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='Todo not found') 
    return todo


@app.put('/todos/{todo_id}')
def update_todo(todo_id:int, updated_todo:TodoCreate) -> Todo:
    todo= get_todo_by_id(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail='Todo not found for update')
    todo.title= updated_todo.title
    todo.description = updated_todo.description
    return todo

@app.delete('/todos/{todo_id}',status_code=204)
def delete_todo(todo_id:int):
    todo = get_todo_by_id(todo_id)
    
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todos.remove(todo)
    return None

@app.patch("/todos/{todo_id}/complete")
def toggle_complete(todo_id: int) -> Todo:
    todo = get_todo_by_id(todo_id)
    
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    todo.completed = not todo.completed
    
    return todo    
  
    