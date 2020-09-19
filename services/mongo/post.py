import pymongo
from services.mongo.connection import client

db = client.jobs

def job(job):
    print(dict(job))
    db.jobs.insert_one(job.dict())