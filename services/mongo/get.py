from services.mongo.response import validate_search, bson_to_json
from services.mongo.connection import client

db = client.jobs

async def job(**search_criteria):
    search_criteria = validate_search(search_criteria)
    jobs_loaded = db.jobs.find(search_criteria,)
    return bson_to_json(jobs_loaded)

async def jobs():
    return bson_to_json(db.jobs.find({}))

async def company(**search_criteria):
    search_criteria = validate_search(search_criteria)
    company_loaded = db.companies.find(search_criteria)
    return bson_to_json(company_loaded)

async def companies():
    return bson_to_json(db.companies.find({}))

async def contact(**search_criteria):
    search_criteria = validate_search(search_criteria)
    company_loaded = db.companies.find(search_criteria)
    return bson_to_json(company_loaded)

