import pymongo
from services.mongo.response import input_to_bson
import services.mongo.post as post
from services.mongo.connection import client

db = client.jobs

async def job(id, job):
    if not job.Company.id:
        job.Company = post.company(job.Company)
    if not job.PrimaryContact.id and job.PrimaryContact.Name:
        job.PrimaryContact = post.contact(job.PrimaryContact)
    db.jobs.update_many(
        {'_id':input_to_bson(id)},
        {'$set':job.dict()}
    )