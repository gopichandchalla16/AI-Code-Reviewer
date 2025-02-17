import streamlit as st
import google.generativeai as genai

# Set up the Google Gemini API Key
api_key = "AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8"  # Replace with your actual API key
genai.configure(api_key=api_key)

# System prompt for AI Code Reviewer
sys_prompt = """You are an expert AI Code Reviewer. Your tasks:

1. Identify the Programming Language: 
   - Detect the programming language used in the provided code.  

2. Code Analysis:
   - Review the code for syntax errors, logical bugs, and security vulnerabilities.  
   - Identify potential performance optimization opportunities.  

3. Issue Reporting:  
   - List all identified issues with severity levels:  
     - Critical: Code-breaking errors or severe security flaws.  
     - High: Major bugs affecting functionality or security.  
     - Medium: Performance inefficiencies or maintainability issues.  
     - Low: Minor improvements, best practices, or style recommendations.  

4. Provide Corrected Code:  
   - Offer a corrected version of the code with fixes applied.  
   - Ensure the revised code maintains or improves functionality.  

5. Detailed Explanations:  
   - Explain each correction clearly and concisely.  
   - Provide reasoning behind optimizations and best practices.  

6. Structured and Readable Output:  
   - Use clear section headers for better readability:  
     ```
     ## Programming Language Identified  
     ## Identified Issues  
     ## Corrected Code  
     ## Explanation and Best Practices  
     ```  
   - Ensure proper formatting of code snippets using Markdown.  

7. Handle Non-Code Inputs Gracefully: 
   - If the input is not valid code, respond politely and request proper code input.  
   - Example: `"It looks like the input is not valid code. Please provide a correct code snippet for review."`  

Follow these steps systematically for accurate and insightful code reviews.  

For non-code inputs, politely request valid code.
"""

gemini_model = genai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Streamlit UI setup
st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")

# Custom CSS styling for aesthetics
st.markdown("""
    <style>
    .main { background-color: #f5f7fb; }
    .header { 
        padding: 2rem; 
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
        color: white; 
        text-align: center;
        border-radius: 12px;
    }
    .stTextArea textarea {
        font-family: 'Fira Code', monospace;
        font-size: 14px;
        background-color: #1e1e1e;
        color: #d4d4d4;
        border-radius: 8px;
        padding: 1rem;
    }
    .stButton button {
        background: linear-gradient(135deg, #4f46e5 0%, #9333ea 100%);
        color: white;
        font-weight: bold;
        padding: 12px 28px;
        border-radius: 25px;
        transition: all 0.3s;
        width: 100%;
        border: none;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 15px rgba(99,102,241,0.3);
    }
    .review-container {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.markdown("""
<div class="header">
    <h1>AI Code Review Assistant 🤖</h1>
    <p>Get instant code reviews with AI</p>
</div>
""", unsafe_allow_html=True)

# Main Content
col1, col2 = st.columns([2, 3], gap="large")

with col1:
    st.subheader("📝 Enter Your Code Below")
    user_code = st.text_area(
        "Code Input",
        placeholder="Paste your Python code here. The AI will identify bugs and suggest fixes."
    )

""", height=400)
    
    analyze_button = st.button("Analyze Code 🚀", use_container_width=True)

with col2:
    if analyze_button and user_code.strip():
        with st.spinner("🔍 Analyzing code. Please wait..."):
            try:
                response = gemini_model.generate_content(f"Code to review:\n```\n{user_code}\n```")
                review_content = response.text
                
                st.markdown("### 📋 Review Results")
                with st.expander("🧩 Identified Issues", expanded=True):
                    st.markdown(review_content.split("## Identified Issues")[1].split("## Corrected Code")[0])
                
                with st.expander("✨ Corrected Code", expanded=True):
                    corrected_code = review_content.split('```')[1]
                    st.code(corrected_code, language="python")
                
                with st.expander("📚 Explanation & Best Practices", expanded=False):
                    st.markdown(review_content.split("## Explanation")[1])
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    elif analyze_button:
        st.warning("Please enter some code to review.")
