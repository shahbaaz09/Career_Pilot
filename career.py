import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def career_advice(resume):

    prompt = f"""
Analyze this resume.

Suggest

1. Best career roles

2. Strengths

3. Weaknesses

4. Skills to Learn

5. Certifications

Resume:

{resume}
"""

    response = model.generate_content(prompt)

    return response.text