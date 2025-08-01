from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
app = FastAPI()

@app.get('/')
def root():
    return FileResponse("index.html")

@app.post('/calculate')
def calculate(num1: int = Form(ge=0, lt=111), num2: int = Form(ge=0, lt=111)):
    return {f'{num1+num2}'}

#  uvicorn app.main:app --reload  <- to start the app

