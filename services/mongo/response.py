from bson.objectid import ObjectId
import datetime

async def input_to_bson(criteria):
    if '_id' in criteria:
        if criteria['_id']:
            criteria['_id'] = ObjectId(criteria['_id'])
    return criteria


async def id_to_bson(id):
    return ObjectId(id)


async def validate_search(criteria):
    # criteria = await input_to_bson(criteria)
    return {
        k:v
        for k, v in criteria.items()
        if v
    }


async def bson_to_json(response):
    formatted_jobs = []
    for job in response:
        for label, value in job.items():
            if isinstance(value, ObjectId):
                job[label] = str(value)
        formatted_jobs.append(job)
    return formatted_jobs


async def populate_date(job):
    for _, status in job.Statuses:
        if status.Completed:
            status.Date = datetime.datetime.now()
    return job

