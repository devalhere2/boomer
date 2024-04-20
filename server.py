from fastapi import FastAPI, Request , status , HTTPException
from fastapi.responses import HTMLResponse,RedirectResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import redis
from contextlib import asynccontextmanager


@asynccontextmanager
async def redis_connection(app: FastAPI):
    redis_client = redis.Redis(host='0.0.0.0', port=6379, db=0,password='gameserver')
    try:
        print(redis_client.ping())
        yield redis_client
        
    finally:
        redis_client.close()

app = FastAPI(lifespan=redis_connection)



server_list = {}
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount('/styles', StaticFiles(directory='styles'), name='styles')



@app.get("/", response_class=HTMLResponse)
async def read_root():
    
    return FileResponse('pages/index.html')

# @app.get("/login", response_class=HTMLResponse)
# async def read_root(request: Request):
#     if request.headers.get('HX-Request') != 'true':
#         return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)

#     return FileResponse('pages/login.html')

@app.get("/uno", response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)

    return FileResponse('pages/uno.html')

@app.get('/unonm', response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)

    return FileResponse('pages/unonm.html')

@app.get('/poker', response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)

    return FileResponse('pages/poker.html')

@app.post('/cserver_form')
async def read_root(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)
    username = data_dict['username']
    create_server_name = data_dict['create_server_name']
    game = data_dict['game']
    
    if 'voicechat' in data_dict:
        voice_chat = 1
    else:
        voice_chat = 0
    
    if 'message' in data_dict:
        message_chat = 1
    else:
        message_chat = 0
    
    if username and create_server_name and game:
        if create_server_name in server_list:
            raise HTTPException(status_code=403, detail="Server Name Already Exists")
        server_list[create_server_name] = {'players': [username], 'game': game ,'voice': voice_chat, 'message': message_chat}
    else:
        raise HTTPException(status_code=403, detail="Enter Username, Server Name and Game")
    print(server_list)
    
@app.post('/jserver_form')
async def read_root(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)
    username = data_dict['username']
    join_server_name = data_dict['join_server_name']
    
    if username and join_server_name:
        if join_server_name in server_list:
            server_list[join_server_name]['players'].append(username)
        else:
            raise HTTPException(status_code=403, detail="Server Name Does Not Exist")
    else:
        raise HTTPException(status_code=403, detail="Enter Username and Server Name")
    print(server_list)
    