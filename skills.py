import re

# Common technical skills (expand this list later)
COMMON_SKILLS = [
    "python", "java", "c", "c++", "javascript", "typescript",
    "html", "css", "react", "angular", "vue",
    "node", "express", "django", "flask", "fastapi",
    "sql", "mysql", "postgresql", "mongodb",
    "numpy", "pandas", "matplotlib", "seaborn",
    "scikit-learn", "tensorflow", "pytorch",
    "machine learning", "deep learning", "nlp",
    "computer vision", "opencv", "yolo",
    "docker", "kubernetes", "aws", "azure", "gcp",
    "git", "github", "linux",
    "power bi", "excel", "tableau"
]


def extract_skills(text):

    text = text.lower()

    found_skills = set()

    for skill in COMMON_SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found_skills.add(skill)

    return sorted(found_skills)


def compare_skills(resume_text, jd_text):

    resume_skills = set(extract_skills(resume_text))
    jd_skills = set(extract_skills(jd_text))

    matched = sorted(resume_skills.intersection(jd_skills))
    missing = sorted(jd_skills - resume_skills)

    return matched, missing