# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# Set up the Google Gemini API Key
api_key = "AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Setting up system prompt for the AI Code Reviewer
sys_prompt = """
You are an AI-powered Python Code Reviewer. Your task is to analyze the provided Python code, identify bugs, errors, or areas of improvement, and provide a corrected version of the code. Follow these steps:
1. Analyze the code for syntax errors, logical errors, or inefficiencies.
2. Provide a detailed explanation of the issues found.
3. Suggest fixes and provide the corrected code snippet.
4. If the code is correct, confirm that no issues were found.
"""

# Initialize the AI model
gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit UI setup
st.title("AI Code Reviewer 🐍")
st.markdown("**Submit your Python code below and get instant feedback on bugs and fixes!**")

# User input for Python code
user_code = st.text_area(
    label="Enter your Python code here:",
    placeholder="Paste your Python code here...",
    height=300
)

# Button to trigger code review
if st.button("Review My Code 🚀"):
    if user_code.strip():
        # Generate response using the Gemini model
        try:
            response = gemini_model.generate_content(
                f"Review the following Python code and provide feedback:\n\n{user_code}"
            )
            st.subheader("Code Review Results:")
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred while processing your request: {e}")
    else:
        st.warning("Please enter some Python code to review.")
