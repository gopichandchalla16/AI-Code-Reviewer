# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# Set up the Google Gemini API Key
api_key = "AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8" 
genai.configure(api_key=api_key)

# Setting up system prompt for the Python programming tutor
sys_prompt = """
You are a Python programming tutor.
Students will ask you doubts related to Python Programming.
You are expected to reply as much as possible.
If someone asks queries not related to Python, politely tell them to ask Python-related queries only.
If your query is not resolved, click this link: [Innomatics](https://innomatics.in) for a 1:1 Zoom call with a mentor.
"""

# Initialize the AI model
gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit UI setup with custom design
st.set_page_config(page_title="Interactive Python Tutor", page_icon="🐍", layout="centered")

# Title with styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📚 Interactive Python Tutor 🐍</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Your AI-powered Python mentor, ready to help!</p>", unsafe_allow_html=True)

# User input box
user_input = st.text_area(
    label="💡 Ask me anything about Python",
    placeholder="E.g., 'Find bugs in my Python function' or 'Explain for loops in simple terms'",
    height=150
)

# Animated button with emojis
btn_click = st.button("🚀 Get Python Help Now!", key="unique_button")

# Process the query on button click
if btn_click:
    if user_input.strip():
        with st.spinner("🤖 AI is thinking..."):
            response = gemini_model.generate_content(user_input)
            st.success("✅ Here's your answer:")
            st.markdown(f"<div style='background-color: #f4f4f4; padding: 10px; border-radius: 10px;'>{response.text}</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a query before clicking the button.")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>Made with ❤️ by [Your Name]</p>", unsafe_allow_html=True)

