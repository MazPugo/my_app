from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello, World v2!"}

@app.get("/health")
def health():
    return {"status": "ok"}





