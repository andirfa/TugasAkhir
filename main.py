from collections import Counter
import dataset_reader
import preprocessing
import processing

def main():
    file_generator = dataset_reader.get_files("training")

    model = processing.DataModel()
    for i in xrange(3):
        article = file_generator.next()
        # for article in file_generator:
        print article.file_name,
        article_token = preprocessing.process(article.data)
        print article_token
        model.put(article, article_token)
    print model


if __name__ == '__main__':
    main()