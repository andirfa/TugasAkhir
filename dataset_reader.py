import os
import re

class Article(object):
    def __init__(self, corpus_type, file_name, content):
        self.corpus_type = corpus_type
        self.file_name = file_name
        self.content = content

def get_files(directory):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    corpus_dir = os.path.join(dir_path, directory)

    for corpus_type in list(os.listdir(corpus_dir)):
        corpus_type_dir = os.path.join(corpus_dir, corpus_type)
        for file_name in list(os.listdir(corpus_type_dir)):
            with open(os.path.join(corpus_type_dir, file_name), mode='r') as a_file:
                content = a_file.read()
            yield Article(corpus_type, file_name, content)

def test(directory):
    for corpus_type, file_name,content in get_files(directory):
        print corpus_type, file_name


if __name__ == '__main__':
    test("training")

