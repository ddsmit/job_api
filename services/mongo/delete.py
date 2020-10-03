from services.mongo.connection import client
from services.mongo.response import id_to_bson

db = client.jobs


def all_jobs():
    db.jobs.delete_many({})


def job(id):
    db.jobs.delete_many({'_id':id_to_bson(id)})


def all_companies():
    db.companies.delete_many({})


def all_contacts():
    db.contacts.delete_many({})