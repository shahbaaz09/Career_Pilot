import fitz
from docx import Document


def extract_pdf_text(uploaded_file):
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()
    return text


def extract_docx_text(uploaded_file):
    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_txt_text(uploaded_file):
    return uploaded_file.read().decode("utf-8")


def extract_text(uploaded_file):

    extension = uploaded_file.name.split(".")[-1].lower()

    if extension == "pdf":
        return extract_pdf_text(uploaded_file)

    elif extension == "docx":
        return extract_docx_text(uploaded_file)

    elif extension == "txt":
        return extract_txt_text(uploaded_file)

    else:
        return "Unsupported File Type"