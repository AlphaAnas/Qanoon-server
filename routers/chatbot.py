
from fastapi import APIRouter
from utils.llama import *



app = APIRouter()
@app.post("/model")

def chatbot(prompt: str):
    try:
        response_text = get_response(prompt)
        return {"message": response_text}
    except Exception as e:
        return {"message": str(e)}

  

