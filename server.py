from fastapi import FastAPI, Request , status
from fastapi.responses import HTMLResponse,RedirectResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

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

@app.get("/login", response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)

    return FileResponse('pages/login.html')

@app.get("/uno", response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)

    return FileResponse('pages/uno.html')

@app.get('/poker', response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)

    return FileResponse('pages/poker.html')