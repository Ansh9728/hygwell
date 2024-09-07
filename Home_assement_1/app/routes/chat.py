from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import HTTPException
from app.services.chat_service import generate_chat_response


class ChatRequest(BaseModel):
    chat_id: str
    user_message: str

class ChatResponse(BaseModel):
    
    bot_response: str


router = APIRouter()

@router.post('/')
def chat(chat_request: ChatRequest):
    try:
        bot_response = generate_chat_response(chat_request.chat_id, chat_request.user_message)
        # return ChatResponse(chat_id=chat_request.chat_id, bot_response=bot_response)
        return {"response":bot_response}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))