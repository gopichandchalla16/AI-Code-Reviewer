# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# Set up the Google Gemini API Key
api_key = "AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Setting up system prompt for the Python programming tutor
sys_prompt = """
You are a Python programming tutor.
Students will ask you doubts related to Python Programming.
You are expected to reply as much as possible.
In case someone asks queries which are not related to Python Programming, politely tell them to ask related queries only.
In case your query is not resolved, feel free to click on this link: innomatics.in to get in touch with our mentor in a 1:1 zoom call
"""

# Initialize the AI model
gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit UI setup
st.title("Interactive Python Tutor")
user_input = st.text_area(label="Enter your query/issue", placeholder="Find bugs in my Python code")

btn_click = st.button("Click Me!")

if btn_click:
    if user_input.strip():
        # Generate response using the Gemini model
        response = gemini_model.generate_content(user_input)
        st.write(response.text)
    else:
        st.warning("Please enter a query.")

