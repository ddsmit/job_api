import pymongo
from services.mongo.response import populate_date
from services.mongo.connection import client
from fastapi.encoders import jsonable_encoder
db = client.jobs


async def job(job):
    if not job.Company.id:
        job.Company = await company(job.Company)
    if not job.PrimaryContact.id and job.PrimaryContact.Name:
        job.PrimaryContact = await contact(job.PrimaryContact)
    job = await populate_date(job)
    job = jsonable_encoder(job)
    db.jobs.insert_one(job)


async def company(company):
    company = jsonable_encoder(company)
    return db.companies.insert_one(company).inserted_id


async def contact(contact):
    contact = jsonable_encoder(contact)
    return db.contacts.insert_one(contact).inserted_id

