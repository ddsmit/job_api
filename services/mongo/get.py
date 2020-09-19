import pymongo
from services.mongo.connection import client
from services.mongo import response

db = client.jobs

def job(
        **kwargs
):
    return [
        job
        for job in db.jobs.find(
            {
                k:v
                for k, v in kwargs.items()
                if v
            },
            {'_id':0}
        )
    ]

def jobs():
    return [job for job in db.jobs.find({},{'_id':0})]

def company(name=None,id=None):
    return

