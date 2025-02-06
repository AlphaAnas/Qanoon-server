from fastapi import FastAPI
from routers import chatbot

app = FastAPI()

app.include_router(chatbot.app)

@app.get("/")
def index():
    return {"message": "Hello, World"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)