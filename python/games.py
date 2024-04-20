from fastapi import APIRouter ,Request ,status
from fastapi.responses import HTMLResponse,RedirectResponse,FileResponse

router = APIRouter()

@router.get("/uno", response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)
    return FileResponse('../pages/uno.html')

@router.get('/unonm', response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)
    return FileResponse('../pages/unonm.html')

@router.get('/poker', response_class=HTMLResponse)
async def read_root(request: Request):
    if request.headers.get('HX-Request') != 'true':
        return RedirectResponse(url='/',status_code=status.HTTP_302_FOUND)
    return FileResponse('../pages/poker.html')
