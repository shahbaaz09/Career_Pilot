import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")


def career_coach(resume_text, jd_text, ats_score, question):

    prompt = f"""
You are CareerPilot AI Coach.

You are an experienced Technical Recruiter, Resume Reviewer, and Career Mentor.

Candidate Resume:

{resume_text}

Job Description:

{jd_text}

Current ATS Score:

{ats_score}

User Question:

{question}

Instructions:

- Answer specifically using the candidate's resume.
- Refer to the job description whenever relevant.
- Give practical, actionable advice.
- If recommending skills, prioritize the most important ones first.
- If suggesting projects, recommend projects relevant to the target role.
- Keep the response concise (150–250 words).
- Use bullet points where appropriate.
- Do not invent qualifications or experience.

Provide only the answer.
"""

    response = model.generate_content(prompt)

    return response.text