from fastapi import APIRouter
from models.job import Job
import config
get, post, update, delete = config.source()

jobs_router = router = APIRouter()

@router.post('')
async def create_job(job: Job):
    return post.job(job)


@router.get('/')
async def get_job(
        id: str = None,
        company_name: str = None,
        title: str = None,
        closed: bool = False,
):
    return get.job(
        _id=id,
        Company=company_name,
        Title=title,
        # closed=closed,
    )


@router.get('')
async def get_jobs():
    return get.jobs()


@router.put('/<id>')
async def update_job(
        id: str,
        job: Job,
):
    return update.job(id, job)


@router.delete('')
async def delete_jobs():
    return delete.all_jobs()


@router.delete('/<id>')
async def delete_job(id):
    return delete.job(id=id)
