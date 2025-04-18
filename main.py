from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel 

app = FastAPI()

# CORS Settings - cross origin resource sharing, when backend connected to frontend
origins = ["*"] # Allow all origins --> domains (can be modified to restrict access)

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True, 
    allow_methods = ["*"], #https methods --> GET, POST
    allow_headers = ["*"] # API keys, header
)

# input request model
class QuestionRequest(BaseModel):
    question: str

# Response body model
class AnswerResponse(BaseModel):
    answer: str


# POST endpoint
@app.post("/ask", response_model=AnswerResponse)
def answer_question(request: QuestionRequest):
    question = request.question
    answer = "Here is a generic answer"
    return {"answer":answer}

# Only runs if you do: python main.py
if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
