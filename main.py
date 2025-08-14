from fastapi import FastAPI
from models import TodoItem

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

# To do app

todos = []

@app.get("/todos")
async def get_todos():
    return todos

@app.post("/todos")
async def create_todo(item: TodoItem):
    todos.append(item)
    return item

@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"error": "Todo not found"}

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, item: TodoItem):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[idx] = item
            return item
    return {"error": "Todo not found"}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for idx, todo in enumerate(todos):
        if todo.id == todo_id:
            del todos[idx]
            return {"message": "Todo deleted"}
    return {"error": "Todo not found"}
