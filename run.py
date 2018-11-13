import os
from app import app

if __name__ == '__main__':
    app.run()

from app.api.V1 import routes
