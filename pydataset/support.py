
from difflib import SequenceMatcher as SM
from collections import Counter
from .locate_datasets import __items_dict


DATASET_IDS = list(__items_dict().keys())
ERROR = ('Not valid dataset name and no similar found! '
         'Try: data() to see available.')


def similarity(w1, w2, threshold=0.5):
    """compare two strings 'words', and
    return ratio of smiliarity, be it larger than the threshold,
    or 0 otherwise.

    NOTE: if the result more like junk, increase the threshold value.
    """
    ratio = SM(None, str(w1).lower(), str(w2).lower()).ratio()
    return ratio if ratio > threshold else 0


def search_similar(s1, dlist=DATASET_IDS, MAX_SIMILARS=10):
    """Returns the top MAX_SIMILARS [(dataset_id : smilarity_ratio)] to s1"""

    similars = {s2: similarity(s1, s2)
                for s2 in dlist
                if similarity(s1, s2)}

    # a list of tuples [(similar_word, ratio) .. ]
    top_match = Counter(similars).most_common(MAX_SIMILARS+1)

    return top_match


def find_similar(query):

    result = search_similar(query)

    if result:
        top_words, ratios = zip(*result)

        print('Did you mean:')
        print(', '.join(t for t in top_words))
        # print(', '.join('{:.1f}'.format(r*100) for r in ratios))

    else:
        raise Exception(ERROR)


if __name__ == '__main__':

    s = 'ansc'
    find_similar(s)
