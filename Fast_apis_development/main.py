from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from app.routes import url_processing
from app.routes import pdf_processing
from app.routes import chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(url_processing.router, prefix="/process_url", tags=['url processing'])
app.include_router(pdf_processing.router, prefix="/process_pdf", tags= ['process pdf'])
app.include_router(chat.router, prefix="/chat", tags=['chat'])


@app.get('/')
def home():
    return {"message":"welcome Users"}


if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)