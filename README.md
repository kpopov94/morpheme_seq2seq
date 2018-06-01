# morpheme_seq2seq
Morpheme Segmentation for the Russian language.

If you use this code, please, cite the paper:
Arefyev N.V., Gratsianova T.Y., Popov K.P. Morphological Segmentation with Sequence to Sequence Neural Network.  In Proceedings of the 24rd International Conference on Computational Linguistics and Intellectual Technologies (Dialogue’2018).


## Requirements
* Python 3.6
* Tensorflow 1.8.0
* seq2seq: https://google.github.io/seq2seq/getting_started/

## Installation
We recommend using Anaconda to work with dependencies. We didn't test our code on Windows.
1. Download and install Anaconda with Python 3.6: https://www.anaconda.com/download
2. Create new environment with python 3.6 and install Tensorflow.
```
conda create -n seq2seq python=3.6
source activate seq2seq
```
To install Tensorflow version compatible with your OS and architecture you should specify the correct channel (-c flag) to download it from. On 64bit Linux the following works for us:
```
conda install -c anaconda tensorflow=1.8
```
On 64bit OS X:
```
conda install -c aaronzs tensorflow=1.8
```


3. Clone seq2seq repository, install.
```
git clone https://github.com/google/seq2seq.git
cd seq2seq
pip install -e .
```
4. Fix import in seq2seq. To do this open seq2seq/contrib/seq2seq/helper.py and replace
```
from tensorflow.contrib.distributions.python.ops import bernoulli
from tensorflow.contrib.distributions.python.ops import categorical
```
with
```
from tensorflow.python.ops.distributions import bernoulli
from tensorflow.python.ops.distributions import categorical
```
5. Clone this repository
```
git clone https://github.com/nvanva/morpheme_seq2seq.git
cd morpheme_seq2seq
```


## Usage
To segment a few words in slang.in using default model run:
```bash
python3 segment.py -s slang.in -o slang.out
```
This will take a few seconds.

To segment 25K test words from test.source using default model run:
```bash
python3 segment.py
```
This will take 5-10 minutes.

To specify your own data and/or model run:
```bash
python3 segment.py -s input_file -m model_dir -o output_file
```
Data must be in compatible format (see test.source).
