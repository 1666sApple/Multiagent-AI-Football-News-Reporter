import os
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from config.tasks import fetch_task, analyze_news_task, compile_newsletter_task, edit_newsletter_task
from config.agents import editor, news_fetcher, analyzer, compiler
import concurrent.futures
import time

load_dotenv()

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

crew = Crew(
    agents=[news_fetcher, analyzer, compiler, editor],
    tasks=[fetch_task, analyze_news_task, compile_newsletter_task, edit_newsletter_task],
    process=Process.sequential
)

def run_crew_with_timeout(timeout=3600):  # 1 hour timeout
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(crew.kickoff, inputs={"topic": "AI for Football Newsletter", "current_time": current_time})
        try:
            result = future.result(timeout=timeout)
            return result
        except concurrent.futures.TimeoutError:
            print(f"The crew's tasks did not complete within {timeout} seconds.")
            return None

result = run_crew_with_timeout()

if result:
    output_file = f"output_{current_time}_football_Newsletter.txt"
    with open(output_file, "w") as f:
        f.write(str(result))
    print(f"Output saved to {output_file}")
else:
    print("The newsletter generation process did not complete successfully.")