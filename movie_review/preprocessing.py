import nltk
import emoji

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

for resource in ["stopwords", "punkt_tab", "wordnet", "omw-1.4"]:
    nltk.download(resource, quiet=True)


def remove_html(text):
    return BeautifulSoup(text, "html.parser").get_text()


def replace_emoji(text):
    return emoji.demojize(text)


stop_words = set(stopwords.words("english"))
stop_words -= {"not", "no", "nor"}


def remove_stopwords(text):
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)


wordnet_lemma = WordNetLemmatizer()


def lemma(tokens):
    return [wordnet_lemma.lemmatize(word) for word in tokens]


def preprocess_text(text):
    text = str(text).lower()
    text = remove_html(text)
    text = replace_emoji(text)
    text = remove_stopwords(text)

    tokens = word_tokenize(text)
    tokens = lemma(tokens)

    return " ".join(tokens)