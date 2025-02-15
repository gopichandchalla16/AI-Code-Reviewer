# Import necessary libraries
import streamlit as st
import google.generativeai as genai

# Set up the Google Gemini API Key
api_key = "AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Setting up system prompt for the AI Code Reviewer
sys_prompt = """
You are an expert AI Code Reviewer. Your tasks:
1. Identify the programming language first
2. Analyze code for bugs, security issues, and optimization opportunities
3. List issues with severity levels (Critical/High/Medium/Low)
4. Provide corrected code with explanations
5. Suggest best practices and optimizations
6. Format output with clear section headers

For non-code inputs, politely request valid code.
"""

# Initialize the AI model
gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit UI setup
st.set_page_config(page_title="AI Code Reviewer 🤖", page_icon=":computer:", layout="wide")

# Custom CSS styling
st.markdown(f"""
    <style>
    .main {{
        background-color: #f5f7fb;
    }}
    .header {{
        padding: 2rem;
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }}
    .stTextArea textarea {{
        font-family: 'Fira Code', monospace;
        font-size: 14px;
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 8px;
    }}
    .stButton button {{
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        font-weight: bold;
        padding: 12px 28px;
        border-radius: 25px;
        border: none;
        transition: all 0.3s;
        width: 100%;
    }}
    .stButton button:hover {{
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(99,102,241,0.3);
    }}
    .review-container {{
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 2rem;
    }}
    .language-badge {{
        padding: 4px 12px;
        border-radius: 20px;
        background: #e0e7ff;
        color: #4f46e5;
        font-weight: 500;
        display: inline-block;
        margin-bottom: 1rem;
    }}
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header">
    <h1 style="margin:0">AI Code Review Assistant 🤖</h1>
    <p style="opacity:0.9; margin:0.5rem 0">Get instant code reviews</p>
</div>
""", unsafe_allow_html=True)

# Main Content
col1, col2 = st.columns([2, 3], gap="large")

with col1:
    st.markdown("### 📝 Fix your Bugs")
    user_code = st.text_area(
        label="Code Input",
        placeholder="// Fix your Bugs here...\nfunction example() {\n  console.log('Hello World!');\n}",
        height=400,
        label_visibility="collapsed"
    )
    
    if st.button("**Analyze Code** 🚀", use_container_width=True):
        if not user_code.strip():
            st.warning("Please enter some code to review")
            st.stop()

with col2:
    if user_code.strip():
        with st.spinner("🔍 Analyzing code. This might take a moment..."):
            try:
                response = gemini_model.generate_content(
                    f"Code to review:\n```\n{user_code}\n```"
                )
                
                with st.container(border=True):
                    st.markdown("### 📋 Review Results")
                    
                    # Process and format the response
                    review_content = response.text
                    
                    # Display in expandable sections
                    with st.expander("🧩 Identified Issues", expanded=True):
                        st.markdown(review_content.split("## Identified Issues")[1].split("## Corrected Code")[0])
                        
                    with st.expander("✨ Corrected Code", expanded=True):
                        st.markdown(f"```\n{review_content.split('```')[1]}\n```")
                        
                    with st.expander("📚 Detailed Explanation", expanded=False):
                        st.markdown(review_content.split("## Detailed Explanation")[1])
                        
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
