import pymongo
from services.mongo.response import populate_date
from services.mongo.connection import client

db = client.jobs


async def job(job):
    if not job.Company.id:
        job.Company = company(job.Company)
    if not job.PrimaryContact.id and job.PrimaryContact.Name:
        job.PrimaryContact = contact(job.PrimaryContact)
    job = populate_date(job)
    db.jobs.insert_one(job.dict())


async def company(company):
    company = company.dict()
    company.pop('id')
    return db.companies.insert_one(company).inserted_id


async def contact(contact):
    return db.contacts.insert_one(contact.dict()).inserted_id

