from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET endpoint
@app.get("/hello")
def read_root():
    return ("Hello from Fastapi")
@app.get("/")
def main():
    return "mainpage"
