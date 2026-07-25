import re
import nltk

# Download only the resources we actually use
resources = [
    ("corpora/stopwords", "stopwords"),
    ("corpora/wordnet", "wordnet"),
]

for path, name in resources:
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(name)

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):

    # Lowercase
    text = text.lower()

    # Remove punctuation and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Simple regex tokenization (no punkt required)
    tokens = re.findall(r"\b[a-zA-Z]+\b", text)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Remove short words
    tokens = [word for word in tokens if len(word) > 2]

    # Lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return " ".join(tokens)
