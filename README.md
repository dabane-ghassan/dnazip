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
sudo python3 setup.py install
```

## Getting started

### GUI

- After installing the package from source or using pip, the interface can be launched simply from the command line:
```
dnazip
```
- If problems occur with the installation, an interface instance can be imported and launched:
```python
from dnazip.interface import Interface
gui = Interface()
gui.main()
```

### Do you want to use just the algorithms?

#### Generating a random DNA sequence

```python
from dnazip.sequence import Sequence
randseq = Sequence.generate(length=5000)
Sequence('/path/to/new/seq').write(randseq)
```
#### Encoding a DNA sequence with Burros-Wheeler + Huffman Coding

```python
from dnazip.encoder import FullEncoder
zip = FullEncoder('path/to/seq')
zip.full_zip()
```

#### Decoding a DNA sequence with Huffman decoding + Reversing Burros-Wheeler transform

```python
from dnazip.decoder import FullDecoder
unzip = FullDecoder('path/to/seq')
unzip.full_unzip()
```

## Documentation

Detailed documentation on the architecture can be found [here](https://dabane-ghassan.github.io/dnazip)

## About

### :scroll: License 
**MIT Licensed** © [Ghassan Dabane](https://github.com/dabane-ghassan), 2021.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/made-with-markdown.svg)](https://forthebadge.com)
[![ForTheBadge uses-git](http://ForTheBadge.com/images/badges/uses-git.svg)](https://GitHub.com/)
[![ForTheBadge uses-badges](http://ForTheBadge.com/images/badges/uses-badges.svg)](http://ForTheBadge.com)
