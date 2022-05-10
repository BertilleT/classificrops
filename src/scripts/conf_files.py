from configparser import ConfigParser

file = 'conf.ini'
config = ConfigParser()
config.read('conf.ini')

print(config.sections())
print(config['classification_source'])
print(list(config['classification_source']))
print(config['classification_source']['path'])

config['classification_source']['path']='test'
print(config['classification_source']['path'])

with open(file, 'w') as configfile:
    config.write(configfile)

