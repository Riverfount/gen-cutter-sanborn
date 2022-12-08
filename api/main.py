from fastapi import FastAPI

from api.business_rules.cutter_table import gen_cutter_code, gen_cutter_table

api = FastAPI()

cutter_table = {}


@api.on_event("startup")
async def startup_event():
    global cutter_table
    cutter_table = gen_cutter_table()


@api.get('/v1/cutter/{last_name}')
def get_cutter_code(last_name: str) -> str:
    cutter_code = gen_cutter_code(last_name)
    return cutter_code


@api.get('/health')
async def health():
    return {'message': 'The API is 100% ok!'}
