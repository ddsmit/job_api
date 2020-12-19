from fastapi import APIRouter, Request
from models.job import Job, JobUpdate
import config
get, post, update, delete = config.source()

jobs_router = router = APIRouter()

@router.post('')
async def create_job(job: Job):
    return await post.job(job)


@router.get('/')
async def get_job(
        id: str = None,
        company_name: str = None,
        title: str = None,
        closed: bool = False,
):
    return await get.job(
        _id=id,
        Company=company_name,
        Title=title,
        # closed=closed,
    )


@router.get('')
async def get_jobs():
    return await get.jobs()


@router.put('/<id>')
async def update_job(
        id: str,
        job: JobUpdate,
):
    return await update.job(id, job)


@router.delete('')
async def delete_jobs():
    return await delete.all_jobs()


@router.delete('/<id>')
async def delete_job(id):
    return await delete.job(id=id)
