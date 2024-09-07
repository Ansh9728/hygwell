from fastapi import UploadFile, File
from fastapi import APIRouter
from fastapi import HTTPException
# from services.pdf_service import process_pdf
from app.services.pdf_service import process_pdf
from typing import List
from app.utils.storage_utils.store_content_json import store_content
import os

router = APIRouter()

@router.post("/")
def upload(files: List[UploadFile] = File(...)):

    try:
        pdf_data = process_pdf(files)

        if pdf_data:

            store_flag = store_content(pdf_data)
            if store_flag:
                
                return {"chat_id":"","message": "PDF Content Processed and Stored Succusfully"}
            
            return {"chat_id": "", "message":"Pdf Not processes"}
            
        return {"chat_id": "", "message":"No any Data in pdf"}

    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))