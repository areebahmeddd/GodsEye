# Core library imports: Environment variables setup
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Access the environment variables
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')