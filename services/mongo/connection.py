import pymongo
import json
import pathlib
import os

try:
    parameters_path = pathlib.Path('parameters', 'mongo.json')
    if not parameters_path.exists():
        parameters_path = pathlib.Path('..', '..', 'parameters', 'mongo.json')
    parameters = json.load(open(parameters_path))
    connection = parameters['Connection']
except:
    connection = os.environ.get('Connection')

client = pymongo.MongoClient(parameters['Connection'])
