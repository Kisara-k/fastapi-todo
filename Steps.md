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
