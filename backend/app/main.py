from fastapi import FastAPI
from dotenv import load_dotenv

from app.middleware.cors import setup_cors
from app.bot.webhook import router as telegram_webhook_router
from app.bot.register_webhook import register_telegram_webhook
from app.bot.application import create_telegram_application

load_dotenv()

app = FastAPI(title="Bika Marketplace API")

setup_cors(app)

app.include_router(telegram_webhook_router)


@app.on_event("startup")
async def startup_event():
    try:
        telegram_application = await create_telegram_application()
        if telegram_application:
            app.state.telegram_application = telegram_application

        await register_telegram_webhook()
    except Exception:
        pass


@app.get("/")
async def root():
    return {"name": "Bika Marketplace", "status": "running"}


@app.get("/health")
async def health():
    return {"status": "ok"}
