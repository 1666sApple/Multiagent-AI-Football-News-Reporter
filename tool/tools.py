import os
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')  # Adjust the path if .env is not in the parent directory
load_dotenv(dotenv_path)

os.environ['SERPER_API_KEY'] = os.environ.get('SERPER_API_KEY')

from crewai_tools import SerperDevTool

serpertool = SerperDevTool()