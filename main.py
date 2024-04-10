from fastapi import FastAPI
from src.routes import contacts

app = FastAPI()

app.include_router(contacts.router, prefix='/api')


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI!"}
