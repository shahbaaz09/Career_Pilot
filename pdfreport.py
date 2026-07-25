from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
        filename,
        ats,
        health,
        matched,
        missing):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph("<b>CareerPilot ATS Report</b>", styles["Title"])
    )

    story.append(
        Paragraph(f"<b>ATS Score:</b> {ats['ats_score']}%", styles["BodyText"])
    )

    story.append(
        Paragraph(f"<b>Rating:</b> {ats['rating']}", styles["BodyText"])
    )

    story.append(
        Paragraph("<br/><b>Resume Health</b>", styles["Heading2"])
    )

    for item, status in health.items():

        mark = "✅" if status else "❌"

        story.append(
            Paragraph(f"{mark} {item}", styles["BodyText"])
        )

    story.append(
        Paragraph("<br/><b>Matched Skills</b>", styles["Heading2"])
    )

    for s in matched:
        story.append(
            Paragraph(s, styles["BodyText"])
        )

    story.append(
        Paragraph("<br/><b>Missing Skills</b>", styles["Heading2"])
    )

    for s in missing:
        story.append(
            Paragraph(s, styles["BodyText"])
        )

    story.append(
        Paragraph("<br/><b>ATS Suggestions</b>", styles["Heading2"])
    )

    for s in ats["suggestions"]:
        story.append(
            Paragraph("• "+s, styles["BodyText"])
        )

    doc.build(story)