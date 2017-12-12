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

    N = 5

    file_generator = dataset_reader.get_files("testing")
    total = 0
    true_count = 0
    # for i in xrange(3):
    for article in file_generator:
        # article = file_generator.next()
        article_token = preprocessing.process(article.content)
        best_n = knn.classify(model, article_token, N)
        best_n_type = [x.corpus_type for x in best_n]
        result_type = knn.pooling(best_n)
        print '---', article.file_name,  '---'
        print 'target->result:', article.corpus_type,'->', result_type
        print 'pool:', best_n_type
        print '------------------------------'

        total += 1
        true_count += 1 if article.corpus_type == result_type else 0

    print ''
    print '>>>>>>>>>>>>>>>>'
    print 'N:', N
    print 'total:', total, 'true:', true_count, 'acc:', true_count * 100.0 /total, '%'
    print '>>>>>>>>>>>>>>>>'

    # print 'emuda', model.get_idf_value('emuda')

if __name__ == '__main__':
    main()
