from processing import calc_tf
from collections import Counter

def remove_worst_match(matches_dict):
    selected = max(matches_dict, key=matches_dict.get)    
    del matches_dict[selected]

def classify(model, query_tokens, n=3):
    best_n_match = dict()
    for article in model.get_articles():
        total = 0
        for token, count in query_tokens.iteritems():
            query_value = calc_tf(count) * model.get_idf_value(token)
            model_value = model.get_tf_value(article, token) * model.get_idf_value(token)
            distance = (query_value - model_value)**2
            total += distance
        # dont need to sqrt total, since we compare the lowest value
        best_n_match[article] = total
        if len(best_n_match) > n:
            remove_worst_match(best_n_match)
    return best_n_match

def pooling(best_matches_dict):
    pool = Counter()
    for match in best_matches_dict:
        pool[match.corpus_type] += 1
    return max(pool, key=pool.get) 

if __name__ == '__main__':
    from collections import Counter
    data = Counter('adqwdasdaadsad')
    print data
    remove_worst_match(data)
    print data
