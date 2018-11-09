import os
from app.api import create_app


config_name = os.getenv('APP_SETTINGS') or 'development'
app = create_app(config_name)