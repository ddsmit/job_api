import pymongo
from services.mongo import get, post
from services.mongo.response import input_to_bson
import services.mongo.post as post
from services.mongo.connection import client

db = client.jobs


async def job(id, job):
    await db.jobs.update_many(
        {'_id': await input_to_bson(id)},
        {'$set':job.dict()}
    )


    # if not await get.company(_id=job.Company.id):
    #     await company(job.Company)
    # if not await get.contact(_id=job.PrimaryContact.id):
    #     await contact(job.PrimaryContact)
    # job = await populate_date(job)
    # job.Company = job.Company.id
    # job.PrimaryContact = job.PrimaryContact.id
    # await db.jobs.insert_one(jsonable_encoder(job))