Create and activate venv

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```
(To exit venv)
```bash
deactivate
```

Refer to the [FastAPI User Guide](https://fastapi.tiangolo.com/tutorial/)

```bash
pip install fastapi
pip install "uvicorn[standard]"
```

Create `main.py`

Instantiate FastAPI and create a get request method.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
```

Run the server

```bash
uvicorn main:app --reload
```

Send a get request with postman (or EchoAPI) to test the endpoint.

## Note: OpenAPI (Swagger) UI

Interactive API documentation automatically generated for your endpoints. When you build an API with FastAPI, it uses the OpenAPI standard (formerly known as Swagger) to describe your API. FastAPI provides a built-in Swagger UI at /docs, where you can:

**View all available endpoints** and their details.
**Test API calls** directly from the browser.
See request/response formats and validation rules.

## To Do App

pydantic provides a BaseModel class that provides data validation
for any class that inherits it.

Make a TodoItem(BaseModel) class in `models.py`, and set up the endpoints.

Note: Todo data is stored as temp, and resets hwne the server is refreshed.