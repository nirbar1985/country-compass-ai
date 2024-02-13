# pylint: disable=line-too-long

import re

import streamlit as st
from dotenv import load_dotenv
from PIL import Image

from agents.conversational_agent import create_agent

load_dotenv('.env')


def display_header_and_image():
    """
    Displays the header information for the chatbot and an image.
    """

    st.markdown('# Multi-Modal Chatbot')
    st.markdown('Powered by Langchain Agents, OpenAI Function Calling, and Streamlit')
    image = Image.open('images/ref.png')
    width, height = image.size
    image = image.resize((width // 2, height // 2))
    st.sidebar.image(image, caption='Image created by DALL·E 3')


def initialize_session():
    """
    Initializes or resets session variables.
    """
    if 'responses' not in st.session_state:
        st.session_state['responses'] = [{'text': 'How can I assist you?', 'image_url': None}]
    if 'requests' not in st.session_state:
        st.session_state['requests'] = []


def display_chat_history():
    """
    Displays the chat history.
    """
    for i, response in enumerate(st.session_state['responses']):
        with st.chat_message('assistant'):
            st.write(response['text'])
            if response['image_url']:
                st.image(response['image_url'], use_column_width=True)

        if i < len(st.session_state['requests']):
            with st.chat_message('user'):
                st.write(st.session_state['requests'][i])


def main():
    display_header_and_image()
    initialize_session()

    if 'agent' not in st.session_state:
        st.session_state.agent = create_agent()
    # container for chat history
    chat_container = st.container()

    # container for user's prompt
    prompt_container = st.container()

    with prompt_container:
        query = st.text_input('Prompt: ', placeholder='Enter your prompt here..')
        if query:
            with st.spinner('Generating Response...'):
                result = st.session_state.agent({'input': query})
                st.session_state.requests.append(query)

                # Extract the URL from the result
                pattern = r'(.*:)\s*\[.*?\]\((.*?)\)'
                match = re.search(pattern, result['output'])
                if match:
                    text_before_link = match.group(1)
                    image_url = match.group(2)

                else:
                    text_before_link = result['output']
                    image_url = None

                # Store the response in the session state
                st.session_state.responses.append({
                    'text': text_before_link,
                    'image_url': image_url,
                })

    with chat_container:
        display_chat_history()


if __name__ == '__main__':
    main()
