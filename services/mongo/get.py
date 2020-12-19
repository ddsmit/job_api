from services.mongo.response import validate_search, bson_to_json
from services.mongo.connection import client

db = client.jobs


async def job(**search_criteria):
    search_criteria = await validate_search(search_criteria)
    print(search_criteria)
    return await bson_to_json(
        await db.jobs.find(search_criteria).to_list(100)
    )


async def jobs():
    return await bson_to_json(
        await db.jobs.find({}).to_list(100)
    )


async def company(**search_criteria):
    search_criteria = await validate_search(search_criteria)
    return await bson_to_json(
        await db.companies.find(search_criteria).to_list(100)
    )


async def companies():
    return await bson_to_json(
        await db.companies.find({}).to_list(100)
    )


async def contact(**search_criteria):
    search_criteria = await validate_search(search_criteria)
    print(search_criteria)
    return await bson_to_json(
        await db.companies.find(search_criteria).to_list(100)
    )

