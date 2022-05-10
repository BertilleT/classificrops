from configparser import ConfigParser
from converter import *

file = 'conf.ini'
config = ConfigParser()
config.read('conf.ini')

'''print(config.sections())
print(config['classification_source'])
print(list(config['classification_source']))
print(config['classification_source']['path'])

config['classification_source']['path']='test'
print(config['classification_source']['path'])
'''

thresholds =[]
num = 1
while num <= 100: 
  num+=1 
  if num % 10 == 0: 
    thresholds.append(num)

for t in thresholds:
    #config['classification_source']['threshold'] = t
    converter(config['classification_source']['path'], config['classification_source']['place'], config['classification_source']['language'],t, config['matching_parameters']['sim_method'])

compareDf = pd.DataFrame (compareList, columns = ['threshold','correctness(%)'])
compareDf.to_csv('../../../../data/FR/compare.csv', index=False)
