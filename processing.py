import cmath
from collections import Counter

class DataModel(object):

    def __init__(self):
        self.__articles = dict()

    def put(self, key, data):
        self.__articles[key] = data

    def get_tf_value(self, article, token):
        tokens = self.__articles[article]
        value = 0 if token not in tokens \
            else 1+cmath.log10(tokens[token])
        return value

    def get_idf_value(self, token):
        D = len(self.__articles)
        df = sum([1 for tokens in self.__articles if token in tokens])
        value = cmath.log10(D/df)

    def get_articles(self):
        for article in self.__articles:
            yield article

    def __str__(self):
        count_type = Counter([article.corpus_type for article in self.__articles])
        return "the model contains {} articles with {} types".format(len(self.__articles),count_type)
