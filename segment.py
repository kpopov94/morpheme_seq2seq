from subprocess import call
import os
import argparse
import logging

def parse_file(words,model_dir,output_file,debug):
    with open(words) as inp, open('___test','w') as test:
        for line in inp:
            test.write(' '.join([c for c in line]))
    with open('./infer_command') as fcommand:
        command=fcommand.read() % (model_dir,'___test','___output')
    call(command, stdout=open(os.devnull, "w"), stderr=open(os.devnull, "w"), shell=True)
    with open('___output') as outpf:
        parsed=''
        for line in outpf:
            parsed += line.replace(' ', '').replace('*', '')[:-1]+'\t'+line.replace(' ', '').replace('*', ' ')
    if output_file is not None:
        with open(output_file, 'w') as outp:
            outp.write(parsed)
    else:
        print(parsed)
    if not debug:
        os.remove('./___test')
        os.remove('./___output')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Morpheme segmentation with seq2seq model')
    parser.add_argument('-m','--model',help='Path to seq2seq model directory',default='./model',dest='model')
    parser.add_argument('-s','--source',help='Path to words for segmentation',default='./test.source',dest='source')
    parser.add_argument('-o','--output',help='Path to the file where predictions will be saved',default='./pred',dest='output')
    parser.add_argument('-debug',action='store_true',dest='debug')
    args=parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)s: %(message)s')
    else:
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
    global logger
    logger=logging.getLogger(__name__)

    logger.info('Segmentation started')
    logger.debug('Source file: %s\nModel directory: %s\nOutput file: %s',args.source,args.model,args.output)
    parse_file(args.source,args.model,args.output,args.debug)
    logger.info('Predictions saved in %s',args.output)