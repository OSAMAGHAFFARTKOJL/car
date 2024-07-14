import streamlit as st
#from langflow.load import run_flow_from_json
import os
from openai import OpenAI

api_key = st.secrets["openai"]["api_key"]


try:
    results = run_flow_from_json("/content/CSA Robot.json", input_value="Hello, World!")
    st.write("Flow Results:", results)
except:
    # Retrieve the API key from environment variables

    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

    # Instantiate the client with the API key
    client = OpenAI(api_key=api_key)

    def generate_response(user_input):
        # Create a chat completion
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" for GPT-4
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        # Access the response content
        return chat_completion.choices[0].message.content

    # Streamlit UI
    st.title("Car Servicing Assistant")

    user_input = st.text_input("Enter your question:")
    if st.button("Submit"):
        response = generate_response(user_input)
        st.write(response)
