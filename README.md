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

### Using the library

#### Generating a random DNA sequence

- A random DNA sequence with an alphabet of ATCGN can be generated for any given length specified in the parameter.

```python
from dnazip.sequence import Sequence
randseq = Sequence.generate(length=5000)
Sequence('/path/to/new/seq').write(randseq)
```
#### Encoding a DNA sequence with Burros-Wheeler + Huffman Coding

- To encode a DNA sequence using BWT and Huffman coding, you can use a FullEncoder object that will save two files to the same directory as the sequence, the Burros-Wheeler transform and the UTF-8 zipped format of the sequence: 
```python
from dnazip.encoder import FullEncoder
encode = FullEncoder('/home/ghassan/M1/gtf.txt')
encode.full_zip()
```
- The attributes of the object can be accessed to see intermediary results:
```python
encode.bw_encoder.rotations # a matrix of string rotations from a sequence
encode.bw_encoder.bwm # The Burros-Wheeler Matrix
encode.bw_encoder.bwt # The Burros-Wheeler Transform

encode.huff_encoder.header # The header of the zip file that contains Huffman codes for each character as well as the sequence binary padding
encode.huff_encoder.binary # The binary sequence of the BW transform
encode.huff_encoder.unicode # 8-bits encoded binary sequence
```
- ***A random sequence of size 1kB was compressed efficiently to 549 bytes.***

#### Decoding a DNA sequence with Huffman decoding + Reversing Burros-Wheeler transform

- To decode a zipped DNA sequence using Huffman decoding and the inverse of BWT, you can use a FullDecoder object that will work in the same manner as the FullEncoder object:
```python
from dnazip.decoder import FullDecoder
decode = FullDecoder('path/to/seq')
decode.full_unzip()
```
- The attributes can also be accessed to see intermediary results:
```python
decode.huff_decoder.header # The header of the zip file that contains Huffman codes for each character as well as the sequence binary padding that where saved when the Huffman tree was created
decode.huff_decoder.unicode # 8-bits encoded sequence
decode.huff_decoder.binary # The binary sequence

decode.bw_decoder.bwm # The Burros-Wheeler reconstructed matrix
decode.bw_decoder.original # The original sequence
```
#### Building the Burros-Wheeler transform using the advanced algorithm

- The BWT can be constructed using a Suffix Array (SA) based algorithm that has a better time and space complexities:

```python
from dnazip.sequence import Sequence
from dnazip.burros_wheeler import BurrosWheeler

seq = Sequence('/home/ghassan/M1/gtf.txt').read()
BurrosWheeler.bwt_advanced(seq)
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
