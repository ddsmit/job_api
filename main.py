from fastapi import FastAPI
from models.job import Job
from services.mongo import get, post

app = FastAPI()

@app.get('/jobs/')
async def get_job(
        company_name: str = None,
        title: str = None,
        closed: bool = False,
):
    return get.job(
        Company=company_name,
        Title=title,
        # closed=closed,
    )

@app.get('/jobs')
async def get_jobs():
    return get.jobs()

@app.post('/jobs/')
async def create_job(job: Job):
    return post.job(job)
