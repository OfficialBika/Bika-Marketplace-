from fastapi import APIRouter

router = APIRouter()


def register_routes(app):
    app.include_router(router)
