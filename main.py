import os
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from config.tasks import fetch_task, analyze_news_task, compile_newsletter_task, edit_newsletter_task
from config.agents import editor, news_fetcher, analyzer, compiler

# Load environment variables from .env file
load_dotenv()

# Get the current time in a suitable format
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Initialize Crew with agents and tasks
crew = Crew(
    agents=[news_fetcher, analyzer, compiler, editor],
    tasks=[fetch_task, analyze_news_task, compile_newsletter_task, edit_newsletter_task],
    process=Process.sequential
)

# Kick off the crew's tasks with input data including 'current_time'
result = crew.kickoff(inputs={"topic": "AI for Football Newsletter", "current_time": current_time})
print(result)
