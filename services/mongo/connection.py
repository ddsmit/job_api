import pymongo
import config

configuration = config.get_config()
connection_string = configuration['Connection']
client = pymongo.MongoClient(connection_string)
