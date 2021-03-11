# dnazip

[![ForTheBadge built-with-science](http://ForTheBadge.com/images/badges/built-with-science.svg)](https://GitHub.com/Naereen/)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-brains.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-grammas-recipe.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/ctrl-c-ctrl-v.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/winter-is-coming.svg)](https://forthebadge.com)

- A Python implementation of ***The Burros-Wheeler Transform (BWT)*** alongside ***Huffman compression*** on DNA sequences.
- Hosted on [GitHub](https://github.com/dabane-ghassan/dnazip)
- Documentation? [**here**]()

## Dependencies

- Python 3.x 
- Tkinter

## Installation

- You can install the package either from pip or from the source code hosted on github.

### With pip

```bash
pip install dnazip
```

### From source

```bash
git clone https://github.com/dabane-ghassan/dnazip.git
cd dnazip
python setup.py install
```

## Getting started

### GUI

### Do you want to use just the algorithms?

#### Generating a random DNA sequence

```python
from dnazip import sequence
randseq = sequence.RandomSequence('/path/to/new/seq', legnth=5000)
randseq.generate()
```

#### Encoding a DNA sequence with Burros-Wheeler + Huffman Coding

```python
from dnazip import encoder
zip = encoder.FullEncoder('path/to/seq')
zip.full_zip()
```

## Documentation

## About

### :scroll: License 
**MIT Licensed** © [Ghassan Dabane](https://github.com/dabane-ghassan), 2021.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/made-with-markdown.svg)](https://forthebadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
