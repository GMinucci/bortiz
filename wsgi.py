import os
from src.main import app as application

if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    application.run(port=port, processes=2)
