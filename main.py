from fastapi import FastAPI
from routes.brand import brand

app = FastAPI()

app.include_router(brand)
