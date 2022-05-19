# converter.py
import argparse
def main(): 
    my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

    my_parser.add_argument('-function',
                        help='the function')

    my_parser.add_argument('-path',
                        help='the path to the source classification')

    my_parser.add_argument('-place',
                        help='the place under study (country/region/lander/etc)')

    my_parser.add_argument('-language',
                        help='the language in which the classification is written')

    my_parser.add_argument('-threshold',
                        help='similarity threshold', action='store_true')

    my_parser.add_argument('-similarity',
                        help='the similarity method chosen')

    # Execute parse_args()
    args = my_parser.parse_args()

    print('If you read this line it means that you have provided '
        'all the parameters')

if __name__ == "__main__":
    main()