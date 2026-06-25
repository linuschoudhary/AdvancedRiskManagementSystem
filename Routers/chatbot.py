from fastapi import APIRouter, Depends,Request
from Chatbot.chatbot import main
import asyncio
from Database import model
from Authentication import role_based_access
router = APIRouter()

access = role_based_access.role_required

@router.post("/chatbot",tags=["ChatBot"])
def chatbot_input(message:str,request:Request,current_user : model.User = Depends(access(role_based_access.level_3))):
    # print("Request:",request.headers)
    auth_header = request.headers.get("Authorization")
    # print("auth_header:",auth_header)
    token = auth_header.split(" ")[1] if auth_header and " " in auth_header else ""
    # print("token:",token)
    return asyncio.run(main(content=message,user_token=token))