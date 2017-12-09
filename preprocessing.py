import re
import cmath
from collections import Counter
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

def remove_non_alphabet(article):
    # non alphabetic removal
    article = re.sub('\n', " ", article.lower())
    article = re.sub(r'-', " ", article)
    article = re.sub(r'([a-z])-([a-z])', r'\1\2', article)
    article = re.sub(r'[^a-z|^ ]', '', article)
    return article
    

def remove_stopwords(article):
    stop_words_remover = StopWordRemoverFactory().create_stop_word_remover()
    removed_article = stop_words_remover.remove(article)
    return removed_article

def stem_word(article):
    stemmer = StemmerFactory().create_stemmer()
    stemmed_words = stemmer.stem(article)
    return stemmed_words

def tokenizing(article):
    article_words = article.split(' ')
    article_token = Counter(article_words)
    return article_token


def process(data):
    article = remove_non_alphabet(data)
    article = remove_stopwords(article)
    article = stem_word(article)
    token = tokenizing(article)
    return token




