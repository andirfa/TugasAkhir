"""
Main script of my TA
"""
import cPickle as pickle
import dataset_reader
import preprocessing
# import processing
import knn

def do_processing():
    # file_generator = dataset_reader.get_files("training")
    # model = processing.DataTable()
    # # for i in xrange(3):
    # #     article = file_generator.next()
    # for article in file_generator:
    #     print article.file_name, '-->'
    #     article_token = preprocessing.process(article.content)
    #     # print article_token
    #     model.put(article, article_token)
    #     # print ''
    # model.build_idf_value()

    # with open('obj/pypy_trainig_result.pkl', 'wb') as file_output:
    #     pickle.dump(model, file_output, pickle.HIGHEST_PROTOCOL)

    with open('obj/pypy_trainig_result.pkl', 'rb') as file_input:
        model = pickle.load(file_input)
    
    return model


def main():
    """
    main function of TA
    """
    model = do_processing()

    file_generator = dataset_reader.get_files("training")
    for i in xrange(3):
        article = file_generator.next()
        article_token = preprocessing.process(article.content)
        best_n = knn.classify(model, article_token)
        best_n_type = [x.corpus_type for x in best_n]
        print '---', article.file_name,  '---'
        print 'target->result:', article.corpus_type,'->', knn.pooling(best_n)
        print 'pool:', best_n_type
        print '------------------------------'

    # print 'emuda', model.get_idf_value('emuda')


if __name__ == '__main__':
    main()
