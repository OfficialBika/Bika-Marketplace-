from fastapi.middleware.cors import CORSMiddleware
import os


def setup_cors(app):
    origins = os.getenv('CORS_ORIGINS', '*').split(',')
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
