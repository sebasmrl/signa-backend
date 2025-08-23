import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.brand import brand

app = FastAPI()


load_dotenv()
frontend_domain = os.getenv("ALLOW_DOMAIN") 

origins = [
    frontend_domain,
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            
    allow_credentials=True,           
    allow_methods=["*"],              
    allow_headers=["*"],              
)


app.include_router(brand)
