import os.path
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


#create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

stopword = [line.rstrip('\n') for line in open('dictionary\\stopwordTalaEdited.txt')]

dir_path = os.path.dirname(os.path.realpath(__file__))
hasil1 = []
data1 = []


def preprocessingData(data):
    hasil = []
    for line in data :
        hasil.append(" ".join(preprocessing(line)))
    return hasil

def preprocessing(artikel):

    # non alphabetic removal
    artikel = re.sub('\n', " ", artikel.lower())
    artikel = re.sub(r'-', " ", artikel)
    artikel = re.sub(r'([a-z])-([a-z])', r'\1\2', artikel)
    artikel = re.sub(r'[^a-z|^ ]', '', artikel)
    # return artikel

    result = []
    # tokenization
    for word in artikel.split() :

        # stopword removal
        if word in stopword:
            word = ""

        # stemming Sastrawi
        # word = stemmer.stem(word)

        if len(word) > 0 :
            result.append(word)
    return result


def stopwordRemoval(token):

    token2 = []
    for i in  range(0, len(token)):
        if token[i] not in stopword:
            token2.append(token[i])
    return token2
