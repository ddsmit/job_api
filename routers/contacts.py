from fastapi import APIRouter
import config
get, post, update, delete = config.source()

contacts_router = router = APIRouter()

@router.get('/<id>')
async def get_contact(
        id: str
):
    return get.contact(_id=id)


@router.delete('')
async def delete_contacts():
    return delete.all_contacts()
