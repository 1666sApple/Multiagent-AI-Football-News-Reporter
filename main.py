import os
import concurrent.futures
import litellm
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from config.tasks import fetch_task, analyze_news_task, compile_newsletter_task, edit_newsletter_task
from config.agents import editor, news_fetcher, analyzer, compiler
import time

# Load environment variables
load_dotenv()

# Check for required API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise EnvironmentError("Error: GOOGLE_API_KEY environment variable is not set.")

# Define model details
MODEL_NAME = 'models/gemini-1.5-flash'
PROVIDER_NAME = 'google'

# Define the current time for file naming
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Initialize Crew instance with agents and tasks
crew = Crew(
    agents=[news_fetcher, analyzer, compiler, editor],
    tasks=[fetch_task, analyze_news_task, compile_newsletter_task, edit_newsletter_task],
    process=Process.sequential
)

# Function to set up the LLM provider with error handling
def get_llm_provider():
    try:
        return litellm.completion(
            model=MODEL_NAME,
            provider=PROVIDER_NAME,
            api_key=GOOGLE_API_KEY
        )
    except litellm.exceptions.BadRequestError as e:
        print(f"Error: Bad request - {str(e)}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while setting up the LLM provider: {str(e)}")
        return None

# Run the Crew process with a timeout
def run_crew_with_timeout(timeout=3600):  # 1 hour timeout
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(crew.kickoff, inputs={"topic": "AI for Football Newsletter", "current_time": current_time})
        try:
            result = future.result(timeout=timeout)
            return result
        except concurrent.futures.TimeoutError:
            print(f"The crew's tasks did not complete within {timeout} seconds.")
            return None
        except Exception as e:
            print(f"An error occurred during the crew execution: {str(e)}")
            return None

# Main execution
if __name__ == "__main__":
    if get_llm_provider():
        result = run_crew_with_timeout()
        if result:
            output_file = f"output_{current_time}_football_Newsletter.txt"
            with open(output_file, "w") as f:
                f.write(str(result))
            print(f"Output saved to {output_file}")
        else:
            print("The newsletter generation process did not complete successfully.")
    else:
        print("Failed to set up the LLM provider. Please check the configuration.")
