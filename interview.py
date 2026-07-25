import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_questions(resume, jd):

    prompt = f"""
You are an experienced Technical Interviewer.

Based on the resume and job description,
generate:

1. 10 Technical Questions

2. 5 HR Questions

3. 5 Project-based Questions

Resume:

{resume}

Job Description:

{jd}
"""

    response = model.generate_content(prompt)

    return response.text