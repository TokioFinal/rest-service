from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routers import auth

app = FastAPI()
app.include_router(auth.router)

@app.get('/healthz')
def healthz():
    return JSONResponse( status_code=200 ,content = {"message": "Everything okay"})