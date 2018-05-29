# morpheme_seq2seq
## Requirements
* Python 3
* Tensorflow 1.3.0
* seq2seq: https://google.github.io/seq2seq/getting_started/

## Installation
We recommend using Anaconda to work with dependencies. We didn't test our code on Windows.
1. Download and install Anaconda with Python 3.6: https://www.anaconda.com/download
2. Create new environment with Tensorflow 1.3
```
conda create -n seq2seq tensorflow=1.3
source activate seq2seq
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
6. 


## Usage
To segment sample data in test.source into morphemes using default model run:
```bash
python3 segment.py
```
To specify your own data and/or model run:
```bash
python3 segment.py -s input_file -m model_dir -o output_file
```
