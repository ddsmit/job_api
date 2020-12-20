from services.mongo.connection import client
from services.mongo.response import id_to_bson

db = client.jobs


async def all_jobs():
    await db.jobs.delete_many({})


async def job(id):
    await db.jobs.delete_many({'_id':id_to_bson(id)})


async def all_companies():
    await db.companies.delete_many({})


async def all_contacts():
    await db.contacts.delete_many({})