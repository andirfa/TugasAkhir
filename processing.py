"""
Script file that hold processing steps of the TA,
contains:
- case folding (to lower)
- non alphabet remover
- stopwords remover
- stem word
- tokenizing
"""

import math
from collections import Counter

def calc_tf(count):
    return 1+math.log10(count)

def calc_idf(N, df):
    return  math.log10(N/df)

class DataTable(object):
    """
    A  Data Table for TF and IDF
    """
    def __init__(self):
        self.__articles = dict()
        self.__idf_table = dict()

    def put(self, key, data):
        self.__articles[key] = data

    def get_tf_value(self, article, token):
        tokens = self.__articles[article]
        value = 0 if token not in tokens \
            else calc_tf(tokens[token])
        return value

    def get_idf_value(self, token):
        tokens = self.__idf_table
        if len(tokens) < 1:
            raise ValueError('IDF table is empty, create using .build_idf_value()')
        else:
            return 0 if token not in tokens else tokens[token]

    def build_idf_value(self):
        all_counter = Counter()
        for article_dict in self.__articles.values():
            all_counter.update(article_dict)

        D = len(self.__articles)
        for key in all_counter:
            df = sum([1 for article in self.__articles.values() \
                if key in article])            
            self.__idf_table[key] = calc_idf(D, df)

    def get_articles(self):
        for article in self.__articles:
            yield article

    def __str__(self):
        count_type = Counter([article.corpus_type for article in self.__articles])
        return "the model contains {} articles with {} types".format(len(self.__articles), count_type)
