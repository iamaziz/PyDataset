# datasets_handler.py
# dataset handling file

import pandas as pd
from .utils import html2text
from .locate_datasets import __items_dict, __docs_dict, __get_data_folder_path

items = __items_dict()
docs = __docs_dict()

# make dataframe layout (of __datasets_desc()) terminal-friendly
pd.set_option('display.max_rows', 170)
pd.set_option('display.max_colwidth', 90)
# for terminal, auto-detect
pd.set_option('display.width', None)


# HELPER

def __filter_doc(raw):
    note = "PyDataset Documentation (adopted from R Documentation. " \
           "The displayed examples are in R)"
    txt = raw.replace('R Documentation', note)
    return txt


def __read_docs(path):
    # raw html
    html = open(path, 'r').read()
    # html handler
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    txt = h.handle(html)

    return txt


# MAIN

def __get_csv_path(item):
    """return the full path of the item's csv file"""
    return items[item]


def __read_csv(item):
    path = __get_csv_path(item)
    df = pd.read_csv(path, index_col=0)
    # display 'optional' log msg "loaded: Titanic <class 'numpy.ndarray'>"
    # print('loaded: {} {}'.format(item, type(df)))
    return df


def __get_doc_path(item):
    return docs[item]


def __print_item_docs(item):
    path = __get_doc_path(item)
    doc = __read_docs(path)  # html format
    txt = __filter_doc(doc)  # edit R related txt
    print(txt)


def __datasets_desc():
    """return a df of the available datasets with description"""
    datasets = __get_data_folder_path() + 'datasets.csv'
    df = pd.read_csv(datasets)
    df = df[['Item', 'Title']]
    df.columns = ['dataset_id', 'title']
    # print('a list of the available datasets:')
    return df
