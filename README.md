# Multi-Modal Chatbot Powered by LangChain Agents, OpenAI's Function Calling, and Streamlit


## Getting Started
Clone the repository, set up the virtual environment, and install the required packages

1. git clone git@github.com:nirbar1985/compibot.git

1. ( In case you have python version 3.11.4 installed in pyenv)
   ```shell script
   pyenv local 3.11.4
   ```


1. Install dependencies
    ```shell script
    poetry install
    ```

1. Enter virtual env by:
    ```shell script
    poetry shell
    ```

## Store your API keys
- Create .env file
- Place your OPENAI_API_KEY into .env file
- Place your SERPAPI_API_KEY into .env file


## Running the Multi-Modal ChatBot
### Kick of the chatbot by running:
```
streamlit run chatbot_ui.py
```
### Pose queries for instance -  
- images of countries
- Information on countries
- Current data
## License
Distributed under the MIT License. See LICENSE.txt for more information.
