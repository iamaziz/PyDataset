
# locate_datasets.py
# locate datasets file paths

from os import path as os_path
from os import walk as os_walk
from os.path import join as path_join
from .dump_data import __setup_db


def __get_data_folder_path():
    # read rdata folder's path from $HOME
    homedir = os_path.expanduser('~')
    # initiate database datafile
    dpath = path_join(homedir, '.pydataset/resources/rdata/')
    if os_path.exists(dpath):
        return dpath
    else:
        # create PYDATASET_HOME and folders
        __setup_db()
        return __get_data_folder_path()

data_path = __get_data_folder_path()


# scan data and documentation folders to build a dictionary (e.g.
# {item:path} ) for each

items = {}
docs = {}
for dirname, dirnames, filenames in os_walk(data_path):

    # store item name and path to all csv files.
    for fname in filenames:
        if fname.endswith('.csv') and not fname.startswith('.'):
            # e.g. pydataset-package/rdata/csv/boot/acme.csv
            item_path = path_join(dirname, fname)
            # e.g acme.csv
            item_file = os_path.split(item_path)[1]
            # e.g. acme
            item = item_file.replace('.csv', '')
            # store item and its path
            items[item] = item_path

    # store item name and path to all html files.
    for fname in filenames:
        if fname.endswith('.html') and not fname.startswith('.'):
            item_path = path_join(dirname, fname)
            item_file = os_path.split(item_path)[1]
            item = item_file.replace('.html', '')
            docs[item] = item_path


def __items_dict():
    return items


def __docs_dict():
    return docs
