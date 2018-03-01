import os
from src.bortiz import app as application


# if __name__ == "__main__":
port = os.environ.get('PORT', 5000)

application.run(port=port)
