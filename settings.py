from os.path import join, dirname
from dotenv import load_dotenv

# Get .env file path
path = join(dirname(__file__), ".env")

# Load .env vars and delete path variable
load_dotenv(path)
del path
