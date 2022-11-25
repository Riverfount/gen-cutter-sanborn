from fastapi import FastAPI

api = FastAPI()


@api.get('/health')
def health():
    return {'message': 'The API is 100% ok!'}
