import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.schemas.gpt.all import Message, GPTResponse
from app.utils.gpt import get_response_from_gpt

app = FastAPI()

origins = [
    "*"
]

# ПОРТ 8055

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "salamaleikum"}


@app.post("/chat")
async def get_gpt_response(message: Message):
    try:
        response = get_response_from_gpt(message.message)
        response_dict = json.loads(response)
        return GPTResponse(**response_dict)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
