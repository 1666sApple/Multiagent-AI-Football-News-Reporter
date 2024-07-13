import os
from dotenv import load_dotenv
from crewai import Task
from tool.tools import serpertool
from config.agents import news_fetcher, editor, analyzer, compiler

# Load environment variables from .env file
load_dotenv()

# Define tasks using CrewAI Task class
fetch_task = Task(
    description=(
        "Find the top European football news stories from the last 24 hours. "
        "The current time is {current_time}."
    ),
    expected_output=(
        "A list of the top European football news story titles, URLs, and a brief summary for each story from the past 24 hours.\n"
    ),
    tools=[serpertool],
    agent=news_fetcher,
    max_duration=300,
)

analyze_news_task = Task(
    description=(
        "Analyze the top European football news stories gathered by the news_fetcher. "
        "Provide a markdown report with significant insights, player quotations, and critical data."
    ),
    expected_output=(
        "A markdown report capturing the heart of each news story, with significant insights, player quotations, and critical data. "
    ),
    tools=[serpertool],
    agent=analyzer,
    max_duration=300,
)

compile_newsletter_task = Task(
    description=(
        "Compile the analyzed European football news stories into a final newsletter. "
        "Ensure the newsletter is aesthetically pleasing, easily navigable, and well-structured."
    ),
    expected_output=(
        "A final newsletter that incorporates expert commentary, insights, and analyzed news pieces on European football, with a consistent design and layout."
    ),
    tools=[serpertool],
    agent=compiler,
    max_duration=300,
)

edit_newsletter_task = Task(
    description=(
        "Edit the final newsletter to ensure it upholds the highest standards of editorial excellence and journalistic integrity. "
        "Make sure the newsletter is engaging, well-structured, and free of errors."
    ),
    expected_output=(
        "An edited newsletter that is engaging, well-structured, and free of errors."
    ),
    tools=[serpertool],
    agent=editor,
    max_duration=300,
)
