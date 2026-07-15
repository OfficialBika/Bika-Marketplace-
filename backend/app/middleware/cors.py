import os
from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app):
    origins = os.getenv(
        "CORS_ORIGINS",
        "http://localhost:3000"
    )

    allow_origins = [
        item.strip()
        for item in origins.split(",")
        if item.strip()
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
