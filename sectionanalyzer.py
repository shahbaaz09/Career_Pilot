def analyze_resume_sections(resume_text):

    text = resume_text.lower()

    sections = {
        "👤 Contact Information": [
            "@",
            "linkedin",
            "github"
        ],

        "🎓 Education": [
            "education",
            "b.e",
            "btech",
            "university",
            "college"
        ],

        "💼 Experience": [
            "experience",
            "internship",
            "worked",
            "intern"
        ],

        "🚀 Projects": [
            "project",
            "developed",
            "implemented",
            "github"
        ],

        "🛠 Technical Skills": [
            "skills",
            "python",
            "java",
            "sql",
            "machine learning",
            "tensorflow",
            "pytorch"
        ],

        "📜 Certifications": [
            "certificate",
            "certification"
        ]
    }

    result = {}

    for section, keywords in sections.items():

        count = sum(
            keyword in text
            for keyword in keywords
        )

        if count >= len(keywords) * 0.7:
            status = "Excellent"
            color = "green"

        elif count >= len(keywords) * 0.4:
            status = "Good"
            color = "orange"

        else:
            status = "Needs Improvement"
            color = "red"

        result[section] = {
            "status": status,
            "color": color
        }

    return result