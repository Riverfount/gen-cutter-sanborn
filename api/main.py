from fastapi import FastAPI

from api.business_rules.cutter_table import gen_cutter_table

api = FastAPI()

cutter_table = {}


@api.on_event("startup")
async def startup_event():
    global cutter_table
    cutter_table = gen_cutter_table()


@api.get('/health')
async def health():
    return {'message': 'The API is 100% ok!'}
