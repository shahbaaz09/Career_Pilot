import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_cover_letter(resume, jd):

    prompt = f"""
Write a professional cover letter
using the following resume and job description.

Resume

{resume}

Job Description

{jd}
"""

    response = model.generate_content(prompt)

    return response.text