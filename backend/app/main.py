from fastapi import FastAPI
from dotenv import load_dotenv
from app.middleware.cors import setup_cors

load_dotenv()

app = FastAPI(title="Bika Marketplace API")

setup_cors(app)

@app.get("/")
async def root():
    return {"name":"Bika Marketplace","status":"running"}

@app.get("/health")
async def health():
    return {"status":"ok"}
