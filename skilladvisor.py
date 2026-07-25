SKILL_GUIDE = {
    "python": {
        "description": "Core programming language for AI, automation, and backend development.",
        "recommendation": "Practice Python daily and build real-world projects."
    },

    "sql": {
        "description": "Essential for working with relational databases.",
        "recommendation": "Learn CRUD operations, Joins, GROUP BY, and subqueries."
    },

    "mysql": {
        "description": "Popular relational database management system.",
        "recommendation": "Build a small CRUD application using MySQL."
    },

    "postgresql": {
        "description": "Enterprise-grade SQL database widely used in production.",
        "recommendation": "Learn PostgreSQL after mastering SQL fundamentals."
    },

    "git": {
        "description": "Version control system used by software teams.",
        "recommendation": "Practice branching, merging, and pull requests."
    },

    "github": {
        "description": "Platform for hosting and showcasing code.",
        "recommendation": "Maintain a clean portfolio with detailed READMEs."
    },

    "docker": {
        "description": "Containerization platform for deploying applications.",
        "recommendation": "Dockerize one AI or web application."
    },

    "fastapi": {
        "description": "High-performance Python framework for APIs.",
        "recommendation": "Deploy one ML model using FastAPI."
    },

    "flask": {
        "description": "Lightweight Python web framework.",
        "recommendation": "Build a portfolio website or REST API."
    },

    "django": {
        "description": "Full-stack Python web framework.",
        "recommendation": "Build an authentication-based web application."
    },

    "aws": {
        "description": "Cloud platform used for hosting and deployment.",
        "recommendation": "Start with EC2, S3, and IAM."
    },

    "azure": {
        "description": "Microsoft cloud platform.",
        "recommendation": "Learn Azure Fundamentals (AZ-900)."
    }
}


def get_skill_advice(skill):

    skill = skill.lower()

    if skill in SKILL_GUIDE:
        return SKILL_GUIDE[skill]

    return {
        "description": "Skill frequently requested in job postings.",
        "recommendation": "Learn the basics and demonstrate it in a project."
    }