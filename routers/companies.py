from fastapi import APIRouter
import config
get, post, update, delete = config.source()

companies_router = router = APIRouter()


@router.get('')
async def get_companies():
    return await get.companies()


@router.get('/<id>')
async def get_company(
        id: str
):
    return await get.company(_id=id)


@router.delete('')
async def delete_companies():
    return await delete.all_companies()

