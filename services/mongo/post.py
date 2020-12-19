from services.mongo.response import populate_date
import services.mongo.get as get
from services.mongo.connection import client
from fastapi.encoders import jsonable_encoder
db = client.jobs


async def job(job):
    if not await get.company(_id=job.Company.id):
        await company(job.Company)
    if not await get.contact(_id=job.PrimaryContact.id):
        await contact(job.PrimaryContact)
    job = await populate_date(job)
    job.Company = job.Company.id
    job.PrimaryContact = job.PrimaryContact.id
    await db.jobs.insert_one(jsonable_encoder(job))


async def company(company):
    await db.companies.insert_one(jsonable_encoder(company))
    return company.id


async def contact(contact):
    await db.contacts.insert_one(jsonable_encoder(contact))
    return contact.id

