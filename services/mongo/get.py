from services.mongo.response import validate_search, bson_to_json
from services.mongo.connection import client
from fastapi.encoders import jsonable_encoder

db = client.jobs

async def job(**search_criteria):
    search_criteria = validate_search(search_criteria)
    jobs_loaded = db.jobs.find(search_criteria,)
    return jsonable_encoder(jobs_loaded)

async def jobs():
    return jsonable_encoder(db.jobs.find({}))

async def company(**search_criteria):
    search_criteria = validate_search(search_criteria)
    company_loaded = db.companies.find(search_criteria)
    return jsonable_encoder(company_loaded)

async def companies():
    return jsonable_encoder(db.companies.find({}))

async def contact(**search_criteria):
    search_criteria = validate_search(search_criteria)
    company_loaded = db.companies.find(search_criteria)
    return jsonable_encoder(company_loaded)

