from fastapi import FastAPI, Request , status , HTTPException
from fastapi.responses import HTMLResponse,RedirectResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import redis


from gameserver import router as gameserver_router
from games import router as games_router


# @asynccontextmanager
# async def redis_connection(app: FastAPI):
#     redis_client = redis.Redis(host='0.0.0.0', port=6379, db=0,password='gameserver')
#     try:
#         yield redis_client
#     finally:
#         redis_client.close()
    

# app = FastAPI(lifespan=redis_connection)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static', StaticFiles(directory='../static'), name='static')
app.mount('/styles', StaticFiles(directory='../styles'), name='styles')
app.mount('/components', StaticFiles(directory='../components'), name='components')

app.include_router(games_router)
app.include_router(gameserver_router)


@app.get("/", response_class=HTMLResponse)
async def read_root():
    return FileResponse('../pages/index.html')

