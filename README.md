# morpheme_seq2seq
## Requirements
* Python 3
* Tensorflow 1.3.0
* seq2seq: https://google.github.io/seq2seq/getting_started/

## Usage
To segment sample data in test.source into morphemes using default model run:
```bash
python3 segment.py
```
To specify your own data and/or model run:
```bash
python3 segment.py -s input_file -m model_dir -o output_file
```
