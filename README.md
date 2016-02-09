## PyDataset
 [![PyPI version](https://badge.fury.io/py/pydataset.svg)](http://badge.fury.io/py/pydataset)

Provides instant access to many datasets right from Python (in pandas DataFrame structure).

### What?

The idea is simple. There are various datasets available out there, but they are scattered in different places over the web.
Is there a quick way (in Python) to access them instantly without going through the hassle of searching, downloading, and reading ... etc?
PyDataset tries to address that question :)


### Usage:

Start with importing `data()`:
```python
from pydataset import data
```
- To load a dataset:
```python
titanic = data('titanic')
```
- To display the documentation of a dataset:
```python
data('titanic', show_doc=True)
```
- To see the available datasets:
```python
data()
```

That's it.
See more [examples](examples).


### Why?

In `R`, there is a very easy and immediate way to access multiple statistical datasets,
in almost no effort. All it takes is one line ` > data(dataset_name)`.
This makes the life easier for quick prototyping and testing.
Well, I am jealous that Python does not have a similar functionality.
Thus, the aim of `pydataset` is to fill that gap.

Currently, `pydataset` has about 757 (mostly numerical-based) datasets, that are based on `RDatasets`.
In the future, I plan to scale it to include a larger set of datasets.
For example,
1) include textual data for NLP-related tasks, and
2) allow adding a new dataset to the in-module repository.


### Installation:

`$ pip install pydataset`

#### Uninstall:

- `$ pip uninstall pydataset`
- `$ rm -rf $HOME/.pydataset`

### Changelog

**0.2.0**

- Add search dataset by name similarity.
- Example:

```python
>>> data('heat')
Did you mean:
Wheat, heart, Heating, Yeast, eidat, badhealth, deaths, agefat, hla, heptathlon, azt
```

**0.1.1**

- Fix: add support to Windows and fix filepaths, issue #1

### Dependency:
- pandas

### Miscellaneous:

- Tested on OSX and Linux (debian).
- Supports both Python 2 (2.7.11) and Python 3 (3.5.1).


#### TODO:
- add textual datasets (e.g. NLTK stuff).
- add samples generators.


#### Thanks to:

- [RDatasets](https://github.com/vincentarelbundock/Rdatasets): R's datasets collection.  
