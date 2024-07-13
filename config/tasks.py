import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from tool.tools import serpertool
from crewai import Task
from agents import news_fetcher, editor, analyzer, compiler

fetch_task = Task(
    description=(
        "Find the top European football news stories from the last 24 hours. The current time is {current_time}."
    ),
    expected_output=(
        "A list of the top European football news story titles, URLs, and a brief summary for each story from the past 24 hours.\n"
        "Example Output:\n"
        "[\n"
        "    {\n"
        "        'title': 'Dramatic Late Winner in Manchester Derby',\n"
        "        'url': 'https://example.com/story1',\n"
        "        'summary': 'A last-minute goal from Marcus Rashford seals a victory for Manchester United against their city rivals...'\n"
        "    },\n"
        "    {\n"
        "        'title': 'Liverpool Confirms New Signing from LaLiga',\n"
        "        'url': 'https://example.com/story2',\n"
        "        'summary': 'Liverpool has officially announced the signing of a high-profile LaLiga player as they prepare for next season...'\n"
        "    },\n"
        "    ...\n"
        "]"
    ),
    tools=[serpertool],
    agent=news_fetcher,
)

analyze_news_task = Task(
    description=(
        "Analyze the top European football news stories gathered by the news_fetcher. "
        "Provide a markdown report with significant insights, player quotations, and critical data."
    ),
    expected_output=(
        "A markdown report capturing the heart of each news story, with significant insights, player quotations, and critical data. "
        "Example Output:\n"
        "# Manchester Derby Analysis\n"
        "## Summary\n"
        "A last-minute goal from Marcus Rashford seals a victory for Manchester United against their city rivals...\n"
        "## Key Insights\n"
        "- Rashford's performance...\n"
        "## Player Quotes\n"
        "- Rashford: 'It was a team effort...'\n"
        "## Data\n"
        "- Possession: 55% for Manchester United..."
    ),
    tools=[serpertool],
    agent=analyzer,
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
)

edit_newsletter_task = Task(
    description=(
        "Edit the final newsletter to ensure it upholds the highest standards of editorial excellence and journalistic integrity. "
        "Make sure the newsletter is engaging, well-structured, and free of errors."
    ),
    expected_output=(
        "An edited newsletter that is engaging, well-structured, and free of errors. "
        "Example Output:\n"
        "The final newsletter with all sections edited and ready for publishing."
    ),
    tools=[serpertool],
    agent=editor,
)