import yaml


with open("yamltest.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

print cfg['login']['user']


