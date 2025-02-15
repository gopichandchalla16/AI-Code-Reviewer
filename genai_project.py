# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# Set up the Google Gemini API Key
api_key = "AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Setting up system prompt for the AI Code Reviewer
sys_prompt = """
You are an AI-powered Python Code Reviewer. Your task is to:
1. Analyze the provided Python code for bugs, errors, or areas of improvement.
2. Identify and list all potential issues in the code.
3. Provide corrected code snippets for each issue.
4. Explain the fixes in a clear and concise manner.

If the input is not Python code, politely ask the user to provide valid Python code for review.
"""

# Initialize the AI model
gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit UI setup
st.title("AI Code Reviewer 🛠️")
st.markdown("""
    <style>
    .stTextArea textarea {
        font-family: monospace;
        font-size: 14px;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 5px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("### Submit your Python code for review")
st.markdown("Enter your Python code below. The AI will analyze it for bugs and provide fixes.")

# Text area for code input
user_code = st.text_area(
    label="Python Code",
    placeholder="Fix your Bugs Here...",
    height=200
)

# Button to trigger code review
btn_click = st.button("Review My Code 🚀")

if btn_click:
    if user_code.strip():
        # Generate response using the Gemini model
        with st.spinner("Analyzing your code... Please wait."):
            response = gemini_model.generate_content(f"Review this Python code and provide fixes:\n\n{user_code}")
        
        # Display the results
        st.markdown("### Code Review Results")
        st.markdown("**Issues Found and Fixes:**")
        st.write(response.text)
    else:
        st.warning("Please enter some Python code to review.")
