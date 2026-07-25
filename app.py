import plotly.graph_objects as go
import streamlit as st
from parser import extract_text
from preprocess import preprocess_text
from similarity import calculate_similarity
from skills import compare_skills
from optimizer import optimize_resume
from interview import generate_questions
from career import career_advice
from coverletter import generate_cover_letter
from ats import calculate_ats_score
from skilladvisor import get_skill_advice
from pdfreport import generate_pdf
from sectionanalyzer import analyze_resume_sections
from coach import career_coach
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="CareerPilot",page_icon="logo.png",layout="wide")


st.markdown("""
<style>

/* Main App */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

/* Buttons */
.stButton>button{
    border-radius:12px;
    height:3em;
    font-weight:600;
}

/* File Uploaders */
[data-testid="stFileUploader"]{
    border:2px dashed #4F8BF9;
    border-radius:12px;
    padding:15px;
}

/* Tabs */
.stTabs [data-baseweb="tab"]{
    font-size:16px;
    font-weight:600;
}

/* Metric Cards */
[data-testid="metric-container"]{
    border-radius:15px;
    padding:15px;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.sidebar.image("logo.png", width=280)
    st.markdown("""
    <div style="text-align:center; padding:20px 0 10px 0;">
        <h1 style="font-size:48px; margin-bottom:5px;">
            AI-Powered Resume Intelligence
        </h1>
        
    </div>
    """, unsafe_allow_html=True)
    st.info(
        "📄 Upload your Resume and Job Description to receive an ATS score, "
        "skill gap analysis, AI-powered resume optimization, interview questions, "
        "cover letter generation, career guidance, and personalized coaching."
    )


    
    st.subheader("📑 Sections")

    st.markdown("""
    - 📊 **Analysis**
    - 🤖 **AI Tools**
    - 💬 **AI Coach**
    """)

    st.divider()

    st.info(
        """
**Version:** 1.0

Powered by Google Gemini
"""
    )

    st.divider()

    st.caption("© 2026 CareerPilot")
st.title(" CareerPilot")
c1,c2=st.columns(2)
with c1:
    resume=st.file_uploader("📄 Upload Resume",type=["pdf","docx"])
with c2:
    jd=st.file_uploader("📋 Upload Job Description",type=["pdf","docx","txt"])

left, center, right = st.columns([8, 3, 8])


with center:
    analyze = st.button(
        "🚀 Analyze Resume",
        use_container_width=True
    )

if resume and jd and analyze:
    rt=extract_text(resume)
    jt=extract_text(jd)
    crt=preprocess_text(rt)
    cjt=preprocess_text(jt)
    
    st.session_state["resume_text"]=rt
    st.session_state["jd_text"]=jt
    st.session_state["clean_resume"]=crt
    st.session_state["clean_jd"]=cjt



    # Calculate Resume Match Score
    score = calculate_similarity(crt, cjt)

    # Compare Skills
    m, ms = compare_skills(rt, jt)

    # Calculate ATS Score
    ats = calculate_ats_score(
        score,
        m,
        ms,
        rt
    )

    
    st.session_state["score"] = score
    st.session_state["matched"] = m
    st.session_state["missing"] = ms
    st.session_state["ats"] = ats


if "resume_text" in st.session_state:

    score = st.session_state["score"]
    matched = st.session_state["matched"]
    missing = st.session_state["missing"]
    ats = st.session_state["ats"]
    tab1, tab2, tab3 = st.tabs([
        "📊 Analysis",
        "🤖 AI Tools",
        "💬 AI Coach"
    ])

    with tab1:
        st.subheader("📊 ATS Dashboard")

        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)

        col1.metric("🎯 Resume Match", f"{score}%")
        col2.metric("📄 ATS Score", f"{ats['ats_score']}%")
        col3.metric("🟢 Matched Skills", len(matched))
        col4.metric("📌 Skill Coverage", f"{ats['skill_coverage']}%")

        st.success(f"⭐ Resume Rating: {ats['rating']}")

        st.subheader("🟢 Proficient Skills")
        for s in st.session_state["matched"]:
            st.success("✔ "+s)
        
        st.subheader("🔴 Missing Skills")
        
        for skill in missing:
            advice = get_skill_advice(skill)
            with st.expander(f"❌ {skill.upper()}"):
        
                st.write("**Description**")
                st.write(advice["description"])
        
                st.write("**Recommendation**")
                st.success(advice["recommendation"])

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=ats["ats_score"],
            title={'text': "ATS Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "darkgreen"},
                'steps': [
                    {'range': [0, 40], 'color': "#ffb3b3"},
                    {'range': [40, 70], 'color': "#ffe699"},
                    {'range': [70, 100], 'color': "#b6fcb6"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': ats["ats_score"]
                }
            }
        ))

        st.plotly_chart(fig, use_container_width=True)
        st.subheader("💡 ATS Suggestions")
        for suggestion in ats["suggestions"]:
            st.info(suggestion)

        st.divider()
    


        import plotly.express as px
        fig = px.pie(
            values=[len(matched), len(missing)],
            names=["Matched", "Missing"],
            hole=0.55,
            title="Skill Coverage"
        )

        st.plotly_chart(fig, use_container_width=True)
        


    with tab2:
        if st.button("✨ Optimize Resume",key="opt"):
            st.text_area("Optimized Resume",optimize_resume(st.session_state["resume_text"],st.session_state["jd_text"]),height=300)
        if st.button("🎤 Generate Interview Questions",key="int"):
            st.text_area("Interview Questions",generate_questions(st.session_state["resume_text"],st.session_state["jd_text"]),height=300)
        if st.button("📩 Generate Cover Letter",key="cover"):
            st.text_area("Cover Letter",generate_cover_letter(st.session_state["resume_text"],st.session_state["jd_text"]),height=300)
        if st.button("🧠 Career Suggestions",key="career"):
            st.text_area("Career Suggestions",career_advice(st.session_state["resume_text"]),height=300)
        


        


       

    with tab3:
        st.header("💬 CareerPilot AI Coach")

        question = st.text_area(
            "Ask anything about your resume"
        )

        if st.button("Ask AI"):

            answer = career_coach(
                st.session_state["resume_text"],
                st.session_state["jd_text"],
                st.session_state["ats"]["ats_score"],
                question
            )

            st.markdown(answer)






else:
    st.info("Upload both files and analyze.")

st.divider()

st.markdown("""
<div style="text-align:center; color:gray; padding:15px;">

<h4> CareerPilot v1.0</h4>
<p>Analyze • Optimize • Get Hired</p>

<p><b>Developed by Mohammad Shahbaaz Shaikh</b></p>

<p>
<a href="https://github.com/shahbaaz09" target="_blank">🐙 GitHub</a> |
<a href="mailto:shahbaazshaikh.work@gmail.com">📧 Email</a>
<p>

<p>Powered by Google Gemini AI • Streamlit</p>

<p>© 2026 CareerPilot. All Rights Reserved.</p>
<p>Kindly give a star on GitHub </p>
</div>
""", unsafe_allow_html=True)
