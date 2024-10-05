import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai
import time

# Load environment variables
load_dotenv()


st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  
    layout="centered",  
)

# Get the Google API key from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Set up the API configuration with the key
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title and welcome message
st.title("🤖 Gemini Pro - ChatBot")
st.write("Welcome to Gemini Pro! Ask me anything and I will try to help you out.")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

# Add LinkedIn logo and link at the bottom of the app
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
st.image("https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg", width=150)  # LinkedIn logo
st.markdown("[Connect with me on LinkedIn!](https://www.linkedin.com/in/abhishek-nangare-3b6ab1241/)", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
