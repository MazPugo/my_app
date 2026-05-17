from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello from Docker!"}

@app.get("/health")
def health():
    return {"status": "ok"}


