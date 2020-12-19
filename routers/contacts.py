from fastapi import APIRouter
import config
get, post, update, delete = config.source()

contacts_router = router = APIRouter()

@router.get('/<id>')
async def get_contact(
        id: str
):
    return await get.contact(_id=id)


@router.delete('')
async def delete_contacts():
    return await delete.all_contacts()
