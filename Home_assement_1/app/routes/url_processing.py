from fastapi import APIRouter
from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import HttpUrl
from app.services.url_service import process_url
from app.utils.storage_utils.store_content_json import store_content


class WebUrl(BaseModel):
    site_url: HttpUrl

router = APIRouter()

@router.post('/')
def process_web_url(request: WebUrl):
    site_url = request.site_url

    try:
        scrapped_data = process_url(site_url)
        
        store_flag = store_content(scrapped_data)

        if store_flag:
            return {"chat_id":"", "message": "URL Content Processed and Stored Succusfully"}
        
        else:
            return {"chat_id":"", "message":"URL Content Not Processe"}


    except HTTPException as e:
        raise HTTPException(status_code=400, detail=str(e))


    # return {"message":"hello world", "data":site_url}