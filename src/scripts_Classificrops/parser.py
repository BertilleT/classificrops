import argparse
import json
from converter import *
from optimal_threshold import *
from view_stats import *


def main(args): 
    parent = Path(__file__).parents[2]
    if args.f == 'converter':
        src_path = parent.joinpath(args.pa)
        if args.t is None :
            args.t = 80
        if args.s is None : 
            args.s = 'token_set_ratio'
        else : 
            converter(src_path,args.pl,args.l,args.t,args.s)
    elif args.f == "optimal_threshold":
        src_path = parent.joinpath(args.pa)
        hd_path = parent.joinpath(args.hd)
        optimal_threshold(src_path, args.pl, args.l,args.s, hd_path)
    elif args.f == "view_stats":
        view_stats(args.path_r, args.path_d, args.path_p, args.path_LPIS_Catalonia, args.path_LPIS_Catalonia)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',
                        choices={'converter', 'optimal_threshold', 'view_stats'},
                        help='the function to be called. There are : converter, optimal_threshold, and view_stats',
                        default='converter'),
    ##converter
    parser.add_argument('-t', 
                        type = int, 
                        help='similarity threshold')

    ##converter and optimal_threshold
    parser.add_argument('-pa',
                        help='the path to the source classification')
    parser.add_argument('-pl',
                        choices={'WL', 'FR', 'CAT'},
                        help='the place under study, it can be a country, region, lander. It can be situated in France, Belgium or Catalonia. ')
    parser.add_argument('-l',
                        choices={'fr', 'cat'},
                        help='the language in which the classification is written')

    parser.add_argument('-s',
                        choices={'basic','ratio','split+ratio','split+ratio+symetric','partial_ratio','token_sort_ratio', 'token_set_ratio'},
                        help='the similarity method chosen to match 2 classes')
    
    ##optimal_threshold
    parser.add_argument('--hd',
                        help='path toward the handmade conversion table if you want to compare the scriptmade and handmade result'
    )

    ##view_stats
    parser.add_argument('--path_r',
                        help='path toward the regions outline shapefile'
    )
    parser.add_argument('--path_d',
                        help='path toward the departments outline shapefile'
    )
    parser.add_argument('--path_p',
                        help='path toward the provincia outline shapefile'
    )
    parser.add_argument('--path_LPIS_Occitania',
                        help='path toward the Occitania LPIS shapefile'
    )
    parser.add_argument('--path_LPIS_Catalonia',
                        help='path toward the Catalonia LPIS shapefile'
    )
    args = parser.parse_args()

    if args.f == 'converter' and  args.pa is None : 
        f = open('options_converter.json', 'rb')
        #argparse_dict = vars(args)
        args_json = argparse.Namespace()
        args_json.__dict__.update(json.load(f))
        args = parser.parse_args(namespace=args_json)

    elif args.f == 'optimal_threshold' and  args.pa is None : 
        f = open('options_optimal_threshold.json', 'rb')
        #argparse_dict = vars(args)
        args_json = argparse.Namespace()
        args_json.__dict__.update(json.load(f))
        args = parser.parse_args(namespace=args_json)
    elif args.f == 'view_stats' and args.path_r is None : 
        f = open('options_view_stats.json', 'rb')
        #argparse_dict = vars(args)
        args_json = argparse.Namespace()
        args_json.__dict__.update(json.load(f))
        args = parser.parse_args(namespace=args_json)

    print(args)
    main(args)