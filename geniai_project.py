# -*- coding: utf-8 -*-
"""GeniAI-Project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10a-Ictfg_Zr10RTjGSmIJrJgzcV88VFi
"""

pip install google-generativeai

!pip install streamlit

"""# Importing Google Gemini AI"""

import google.generativeai as genai

"""Setting up the API Key"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8")

"""Available Models"""

for m in genai.list_models():
  print(m)

"""Prompting the Gemini Model"""

# pick a model
model = genai.GenerativeModel(model_name="models/learnlm-1.5-pro-experimental")

user_prompt = """Create a fictional debate between Batman and Spider man"""

# Pass the user prompt to the model
response = model.generate_content(user_prompt)

# Print the response
print(response)

from IPython.display import Markdown

Markdown(response.text)

import google.generativeai as genai
from IPython.display import Markdown

genai.configure(api_key="AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8")

sys_prompt = """You are a Python rogramming tutuor. You can only resolove Python Programming related Queries
            In case if someone asks as queries which are not related to Python Programming, politely tell them to ask related queries only
"""

model = genai.GenerativeModel(model_name="models/learnlm-1.5-pro-experimental",system_instruction=sys_prompt)

user_prompt = input("Enter the query: ")

response = model.generate_content(user_prompt)

Markdown(response.text)

import google.generativeai as genai
from IPython.display import Markdown

genai.configure(api_key="AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8")

sys_prompt = """You are a Python Programming tutuor. You can only resolove Python Programming related Queries
            In case if someone asks as queries which are not related to Python Programming, politely tell them to ask related queries only
"""

model = genai.GenerativeModel(model_name="models/learnlm-1.5-pro-experimental",system_instruction=sys_prompt)

user_prompt = input("Enter the query: ")

response = model.generate_content(user_prompt)

Markdown(response.text)

!pip install streamlit  # Install streamlit within the current kernel session

import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyDsDuCqRADUrl1XG7_VxZDtd_nTswxEmh8")

sys_prompt = """You are a Python programming tutor.
               Students will ask you doubts related to Python Programming.
               You are expected to reply as much as it is possible.
               In case if someone asks queries which are not related to Python Programming, politely tell them to ask related queries only.
               In case if your query is not resolved, feel free to click on this link:
                innomatics.in to get in touch with our mentor in a 1:1 zoom call"""

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("Interactive Python Tutor")

user_input = st.text_area(label="Enter your query/issue", placeholder="Explain the concept of for loops")

btn_click = st.button("Click Me!")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)

!jupyter nbconvert --to script your_notebook.ipynb

