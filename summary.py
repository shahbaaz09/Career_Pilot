def generate_resume_summary(
    ats,
    matched,
    missing,
):

    score = ats["ats_score"]

    if score >= 85:
        level = "excellent"
    elif score >= 70:
        level = "strong"
    elif score >= 55:
        level = "average"
    else:
        level = "needs significant improvement"

    strengths = []

    if len(matched) >= 5:
        strengths.append("good technical skill alignment")


    if missing:
        weaknesses.append(
            f"missing important skills such as {', '.join(missing[:4])}"
        )

    

    summary = f"""
### 

Your resume  **{level}** for the selected job role with an estimated **ATS score of {score}%**.

**Strengths**
- {chr(10).join(['• '+s for s in strengths]) if strengths else '• Basic resume structure is present.'}

**Areas to Improve**
- {chr(10).join(['• '+w for w in weaknesses]) if weaknesses else '• No major weaknesses detected.'}

**Overall Recommendation**

Your profile is suitable for entry-level software, AI/ML, or Python-related positions. Improving the missing technical skills, adding measurable project outcomes, and gaining more hands-on experience will significantly increase your chances of passing ATS screening and technical interviews.
"""

    return summary