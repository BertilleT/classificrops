from configparser import ConfigParser
from converter import *
from optimal_threshold import *
import sys

file = 'conf.ini'
config = ConfigParser()
config.read('conf.ini')

def main() :
  script_name = sys.argv[0]
  fct = sys.argv[1]
  config['classification_source']['path'] = sys.argv[2]
  config['classification_source']['place'] = sys.argv[3]
  config['classification_source']['language'] = sys.argv[4]
  config['matching_parameters']['threshold'] = sys.argv[5]
  config['matching_parameters']['sim_method'] = sys.argv[6]

  if fct == '-c':
    converter(config['classification_source']['path'], config['classification_source']['place'], config['classification_source']['language'],config['matching_parameters']['threshold'], config['matching_parameters']['sim_method'])
  elif fct == '-t':
    optimal_threshold(config['classification_source']['path'], config['classification_source']['place'], config['classification_source']['language'],config['matching_parameters']['sim_method'])
  else:
    return print('The arguments are not correct. Please, type converter.py -h to get advices.')



