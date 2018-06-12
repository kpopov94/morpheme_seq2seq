import argparse
import logging
from subprocess import call


def train_model(conf1, conf2, vocab_source, vocab_target, source, target, source_dev, target_dev, batch_size, train_steps,
                output_dir):
    with open('./train_command') as c_file:
        command = c_file.read() % (conf1, conf2, vocab_source, vocab_target, source, target, source_dev, target_dev,
                                   batch_size, train_steps, output_dir)
    logger.debug(command)
    call(command, shell=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Training seq2seq model for morpheme segmentation')
    parser.add_argument('-c1', '--conf1', help='Path to seq2seq training options',
                        default='./train_configs/nmt_medium.yml', dest='conf1')
    parser.add_argument('-c2', '--conf2', help='Path to seq2seq training preferences',
                        default='./train_configs/train_seq2seq.yml', dest='conf2')
    parser.add_argument('-vs', '--vocab_source', help='Path to the vocab.source file', default='./vocab.train.source',
                        dest='vocab_source')
    parser.add_argument('-vt', '--vocab_target', help='Path to the vocab.target file', default='./vocab.train.target',
                        dest='vocab_target')
    parser.add_argument('-s', '--source', help='Path to source file', default='./train.source',
                        dest='source')
    parser.add_argument('-t', '--target', help='Path to target file', default='./train.target',
                        dest='target')
    parser.add_argument('-sd', '--source_dev', help='Path to source_dev file', default='./train.source',
                        dest='source_dev')
    parser.add_argument('-td', '--target_dev', help='Path to target_dev file', default='./train.target',
                        dest='target_dev')
    parser.add_argument('-b', '--batch_size', help='Batch size', default='32',
                        dest='batch_size')
    parser.add_argument('-ts', '--train_steps', help='Train steps', default='100000',
                        dest='train_steps')
    parser.add_argument('-o', '--output', help='Directory for saving model', default='./new_model',
                        dest='output_dir')
    parser.add_argument('-debug', action='store_true', dest='debug')
    args = parser.parse_args()

    conf1 = args.conf1
    conf2 = args.conf2
    vocab_source = args.vocab_source
    vocab_target = args.vocab_target
    source = args.source
    target = args.target
    source_dev = args.source_dev
    target_dev = args.target_dev
    batch_size = args.batch_size
    train_steps = args.train_steps
    output_dir = args.output_dir
    debug = args.debug

    if debug:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    global logger
    logger = logging.getLogger(__name__)

    logger.info('Training started')
    train_model(conf1, conf2, vocab_source, vocab_target, source, target, source_dev, target_dev, batch_size,
                train_steps, output_dir)
    logger.info('Training finished')
