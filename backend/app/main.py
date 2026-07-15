from fastapi import FastAPI
from dotenv import load_dotenv

from app.middleware.cors import setup_cors
from app.bot.webhook import router as telegram_webhook_router
from app.bot.register_webhook import register_telegram_webhook

load_dotenv()

app = FastAPI(title="Bika Marketplace API")

setup_cors(app)

app.include_router(telegram_webhook_router)


@app.on_event("startup")
async def startup_event():
    try:
        await register_telegram_webhook()
    except Exception:
        pass


@app.get("/")
async def root():
    return {"name": "Bika Marketplace", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "ok"}
