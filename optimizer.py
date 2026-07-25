import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def optimize_resume(resume_text, jd_text):

    prompt = f"""
You are an expert ATS Resume Reviewer.

Task:

Rewrite the resume professionally.

Rules:

1. Never invent experience.
2. Never add fake skills.
3. Improve grammar.
4. Improve bullet points.
5. Tailor the wording according to the Job Description.
6. Keep everything truthful.

Resume:

{resume_text}

Job Description:

{jd_text}

Return only the improved resume.
"""

    response = model.generate_content(prompt)

    return response.text