import re


def check_resume_health(resume_text):

    checks = {}

    text = resume_text.lower()

    # Email
    checks["Email"] = bool(
        re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", resume_text)
    )

    # Phone
    checks["Phone"] = bool(
        re.search(r'(\+?\d{1,3}[\s-]?)?(\(?\d{3,5}\)?[\s-]?)?\d{3,5}[\s-]?\d{4,6}', resume_text)
    )

    # LinkedIn
    checks["LinkedIn"] = "linkedin" in text

    # GitHub
    checks["GitHub"] = "github" in text

    # Skills
    checks["Skills Section"] = "skills" in text

    # Projects
    checks["Projects Section"] = "project" in text

    # Education
    checks["Education"] = "education" in text

    # Experience
    checks["Experience"] = (
        "experience" in text or
        "internship" in text
    )

    # Certifications
    checks["Certifications"] = (
        "certificate" in text or
        "certification" in text
    )

    # Resume Length
    checks["Good Resume Length"] = len(resume_text.split()) >= 250

    return checks