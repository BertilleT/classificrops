#parser_2
import argparse
from ast import arg 

parser = argparse.ArgumentParser()

parser.add_argument('-f',
                    help='the function : converter, optimal_threshold, percentages, evolution, or map')

parent_parser = argparse.ArgumentParser(add_help=False)

parent_parser.add_argument('-pa',
                              help='the path to the source classification')
parent_parser.add_argument('-pl',
                              help='the place under study')
parent_parser.add_argument('-lg', 
                              help='the language in which the classification is written')

converter_parser = argparse.ArgumentParser(parents=[parent_parser])
converter_parser.add_argument('-t', 
                    type = int, 
                    help='similarity threshold')

optimal_threshold_parser = argparse.ArgumentParser(parents=[parent_parser])
optimal_threshold_parser.add_argument('-s',
                    help='the similarity method chosen')

parser.parse_args()