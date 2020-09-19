import pymongo
import json
import pathlib

parameters_path = pathlib.Path('parameters', 'mongo.json')

if not parameters_path.exists():
    parameters_path = pathlib.Path('..','..','parameters', 'mongo.json')

parameters = json.load(open(parameters_path))
client = pymongo.MongoClient(parameters['Connection'])
