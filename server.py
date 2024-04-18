from fastapi import FastAPI, Request , status , HTTPException
from fastapi.responses import HTMLResponse,RedirectResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
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

@app.post('/server_form')
async def read_root(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)
    
    if data_dict['username'] and data_dict['create_server_name'] and data_dict['game']:
        if data_dict['create_server_name'] in server_list:
            raise HTTPException(status_code=403, detail="Server Name Already Exists")
        server_list[data_dict['create_server_name']] = data_dict
    elif data_dict['username'] and data_dict['join_server_name']:
        if data_dict['join_server_name'] in server_list:
            server_list[data_dict['join_server_name']]['players'].append(data_dict['username'])
        else:
            raise HTTPException(status_code=403, detail="Server Name Does Not Exist")
    else:
        raise HTTPException(status_code=403, detail="Enter Username, Server Name and Game")
    print(server_list)
    