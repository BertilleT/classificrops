# converter.py
import argparse
from converter import *
from optimal_threshold import *

#my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
my_parser = argparse.ArgumentParser(description = 'arguments for converter tool')

my_parser.add_argument('-f',
                    help='the function', 
                    required = True)

my_parser.add_argument('-pa',
                    help='the path to the source classification', 
                    required = True)

my_parser.add_argument('-pl',
                    help='the place under study, it can be a country, region, lander', 
                    required = True)

my_parser.add_argument('-l',
                    help='the language in which the classification is written',
                    required = True)

my_parser.add_argument('-s',
                    help='the similarity method chosen', 
                    required=True)

my_parser.add_argument('-t', 
                    type = int, 
                    help='similarity threshold')

# Execute parse_args()
args = my_parser.parse_args()

print('If you read this line it means that you have provided '
    'all the parameters')

if args.f == 'converter':
    print('the function called is converter')
    if args.t is not None:
        converter(args.pa,args.pl,args.l, args.t, args.s)
    else: 
        print("you forgot to set a threshold value. For example -t 90")
elif args.f == 'optimal_threshold' :
    print('the function called is optimal_threshold')
    optimal_threshold(args.pa,args.pl,args.l,args.s)

#def test(**kargs):
#    if kargs['fct'] == 'converter':
#        converter()