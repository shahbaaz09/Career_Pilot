import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):

    # lowercase
    text = text.lower()

    # remove punctuation and numbers
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # tokenize
    tokens = word_tokenize(text)

    # remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # remove very short words
    tokens = [word for word in tokens if len(word) > 2]

    # lemmatization
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # join again
    cleaned_text = " ".join(tokens)

    return cleaned_text