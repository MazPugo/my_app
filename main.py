from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=[
        "myappguru.net",
        "www.myappguru.net",
        "localhost",
        "testserver",
        "127.0.0.1",
    ]
)


@app.get("/")
def hello_world():
    return {"message": "Hello World!"}


@app.get("/health")
def health():
    return {"status": "ok"}
