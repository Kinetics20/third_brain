from fastapi import FastAPI


app = FastAPI(
    title='Third Brain API',
    version='0.0.1',
    desription='Third Brain',
)

@app.get('/health')
async def healthcheck():
    return {'status': 'OK'}
