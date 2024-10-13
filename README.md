# Multiagent AI Football News Reporter

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

This project is an AI-driven application designed to fetch, analyze, compile, and edit the latest European football news into a structured and engaging newsletter. It leverages multiple agents, each with a specific role, to automate the entire process from news gathering to newsletter creation.

## Key Features
- **Automated News Gathering:** Efficiently fetch the latest European football news using multiple agents.
- **Multi-Agent Architecture:** Specialized agents for different tasks ensure optimal performance and organization.
- **Analysis and Compilation:** Analyze and compile news articles into a structured and engaging newsletter format.
- **Easy Setup:** Quick installation process with a straightforward configuration.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)
- [Contributing](#contributing)

## Installation

1. **Clone the repository:**

    ```sh
    cd Multiagent-AI-Football-News-Reporter
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following environment variable:

    ```sh
    SERPER_API_KEY=your_serper_api_key_here
    ```

## Usage

1. **Run the main script:**

    ```sh
    python3 main.py
    ```

    The script will start the process of fetching, analyzing, compiling, and editing the newsletter based on the latest European football news.

## Project Structure

```plaintext
root/
├── config/
│   ├── __init__.py
│   ├── agents.py
│   ├── tasks.py
├── tool/
│   ├── __init__.py
│   ├── tools.py
├── .env
├── main.py
├── requirements.txt
```

- config/: Contains configuration files for tasks and agents.
    - agents.py: Defines the agents used in the project.
    - tasks.py: Defines the tasks that will be executed by the agents.
- tool/: Contains tools used by the agents.
    - tools.py: Defines the serpertool used for fetching news.
- main.py: The main entry point of the application.


## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

## Acknowledgements
- Special thanks to the developers of the **Serper API** for providing the news-fetching capabilities that power this application.
- Gratitude to the **python-dotenv** library for enabling easy management of environment variables.
- Appreciation for **crewai** and **crewai_tools** for their contributions to the project, enhancing the overall functionality.
- Thanks to the **Langchain** and **langchain_google_genai** libraries for streamlining the integration of language models in the application.
- Recognition of the **Langchain community** for their support and resources, helping to advance the project.
- Thanks to the open-source community for their invaluable contributions, resources, and support that made this project possible.
- Appreciation to football enthusiasts for inspiring the creation of a platform dedicated to delivering the latest news in an engaging format.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## Author

This project is maintained by [1666sApple](https://github.com/1666sApple).
