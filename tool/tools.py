import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
load_dotenv(dotenv_path)

# Check if the SERPER_API_KEY environment variable is set
if 'SERPER_API_KEY' in os.environ:
    os.environ['SERPER_API_KEY'] = os.environ.get('SERPER_API_KEY')
else:
    print("SERPER_API_KEY environment variable is not set.")

# Initialize SerperDevTool from crewai_tools module
serpertool = SerperDevTool(timeout=60)
