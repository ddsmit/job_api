from fastapi import FastAPI
from routers.jobs import jobs_router
from routers.companies import companies_router
from routers.contacts import contacts_router


app = FastAPI()

app.include_router(
    jobs_router,
    prefix='/jobs',
    tags=['jobs'],
)

app.include_router(
    companies_router,
    prefix='/companies',
    tags=['companies'],
)

app.include_router(
    contacts_router,
    prefix='/contacts',
    tags=['contacts'],
)