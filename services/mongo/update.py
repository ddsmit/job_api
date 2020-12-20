from services.mongo.response import input_to_bson
from services.mongo.connection import client

db = client.jobs


async def job(id, job):
    await db.jobs.update_many(
        {'_id': await input_to_bson(id)},
        {'$set':job.dict()}
    )