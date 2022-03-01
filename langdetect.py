def get_parser():
    parser = argparse.ArgumentParser ()
    parser.add_argument("-i", " --input", help="Input data in csv format ",type = str)
    parser.add_argument("-v", "--voc_size", help="Vocabulary size", type=int)
    parser.add_argument("-a", "--analyzer", help="Tokenization level : {word , char }", type=str, choices=[’word’,’char ’])
r e t u r n parser