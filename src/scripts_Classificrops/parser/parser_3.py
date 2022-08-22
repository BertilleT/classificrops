# converter.py
import argparse
#from ast import arg
from scripts_Classificrops.converter_v2 import *
import json


def main(args): 
    converter(args.pa,args.pl,args.l,args.t,args.s)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-pa',
                        help='the path to the source classification')
    parser.add_argument('-pl',
                        choices={'WL', 'FR', 'CAT'},
                        help='the place under study, it can be a country, region, lander. It can be situated in France, Belgium or Catalunya. ')
    parser.add_argument('-l',
                        choices={'fr', 'cat'},
                        help='the language in which the classification is written')
    parser.add_argument('-t', 
                        type = int, 
                        help='similarity threshold')
    parser.add_argument('-s',
                        choices={'basic','ratio','split+ratio','split+ratio+symetric','partial_ratio','token_sort_ratio', 'token_set_ratio'},
                        help='the similarity method chosen')

    args = parser.parse_args()

    if args.pa is None : 
        f = open('options.json', 'rb')

        #argparse_dict = vars(args)
        args_json = argparse.Namespace()
        args_json.__dict__.update(json.load(f))
        args = parser.parse_args(namespace=args_json)

    print(args)
    main(args)