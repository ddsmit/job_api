import pymongo
from services.mongo.connection import client

db = client.jobs

def build_test_db():
    db.jobs.drop()
    jobs = [
        # {
        #     'Company':'Lowes',
        #     'Title':'Data Engineer',
        #     'Applied':True,
        #     'Closed':False,
        # },
        # {
        #     'Company':'Cigna',
        #     'Title':'Data Analyst',
        #     'Applied':True,
        #     'Closed':False,
        # },
        # {
        #     'Company': 'Google',
        #     'Title': 'Software Engineer',
        #     'Applied': True,
        #     'Closed': True,
        # },
    ]
    db.jobs.insert_many(jobs)


if __name__ == "main":
    build_test_db()