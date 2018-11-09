import os
from app.api import create_app


config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)