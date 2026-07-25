import re


def calculate_ats_score(match_score, matched_skills, missing_skills, resume_text):

    score = 0

    suggestions = []

    # -------------------------
    # 1. Resume Similarity (35)
    # -------------------------

    similarity_score = min(match_score, 100)

    score += similarity_score * 0.35

    # -------------------------
    # 2. Skill Coverage (25)
    # -------------------------

    total = len(matched_skills) + len(missing_skills)

    if total:
        skill_coverage = (len(matched_skills) / total) * 100
    else:
        skill_coverage = 0

    score += skill_coverage * 0.25

    # -------------------------
    # 3. Resume Length (10)
    # -------------------------

    words = len(resume_text.split())

    if words >= 350:
        score += 10
    elif words >= 250:
        score += 8
    elif words >= 150:
        score += 5
    else:
        suggestions.append(
            "Resume is quite short. Aim for at least 300–500 words."
        )

    # -------------------------
    # 4. Projects (10)
    # -------------------------

    project_keywords = [
        "project",
        "projects",
        "github",
        "developed",
        "implemented",
        "built"
    ]

    if any(k in resume_text.lower() for k in project_keywords):
        score += 10
    else:
        suggestions.append(
            "Add academic or personal projects."
        )

    # -------------------------
    # 5. Education (5)
    # -------------------------

    education_keywords = [
        "bachelor",
        "engineering",
        "university",
        "college",
        "b.e",
        "btech",
        "education"
    ]

    if any(k in resume_text.lower() for k in education_keywords):
        score += 5
    else:
        suggestions.append(
            "Include your education section."
        )

    # -------------------------
    # 6. Experience (5)
    # -------------------------

    experience_keywords = [
        "internship",
        "experience",
        "worked",
        "intern"
    ]

    if any(k in resume_text.lower() for k in experience_keywords):
        score += 5
    else:
        suggestions.append(
            "Mention internships or practical experience."
        )

    # -------------------------
    # 7. Contact Info (5)
    # -------------------------

    email = re.search(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        resume_text
    )

    phone = re.search(
        r'(\+?\d{1,3}[\s-]?)?(\(?\d{3,5}\)?[\s-]?)?\d{3,5}[\s-]?\d{4,6}',
        resume_text
    )

    if email and phone:
        score += 5
    else:
        suggestions.append(
            "Include a professional email and phone number."
        )

    # -------------------------
    # 8. Resume Sections (5)
    # -------------------------

    sections = [
        "skills",
        "education",
        "projects",
        "experience"
    ]

    found = sum(
        s in resume_text.lower()
        for s in sections
    )

    score += (found / len(sections)) * 5

    # -------------------------
    # Missing Skills
    # -------------------------

    if missing_skills:

        suggestions.append(
            "Consider learning: " +
            ", ".join(missing_skills)
        )

    score = round(min(score, 100))

    if score >= 90:
        rating = "Excellent ⭐⭐⭐⭐⭐"
    elif score >= 80:
        rating = "Very Good ⭐⭐⭐⭐"
    elif score >= 70:
        rating = "Good ⭐⭐⭐"
    elif score >= 65:
        rating = "Average ⭐⭐"
    else:
        rating = "Needs Improvement "

    return {

        "ats_score": score,

        "skill_coverage": round(skill_coverage, 1),

        "rating": rating,

        "suggestions": suggestions

    }