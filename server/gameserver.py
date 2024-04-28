from fastapi import APIRouter ,Request ,HTTPException


router = APIRouter()
@router.post('/cserver_form')
async def read_root(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)
    username = data_dict['username']
    create_server_name = data_dict['create_server_name']
    game = data_dict['game']
    print(data_dict)
    voice_chat = 1 if 'voicechat' in data_dict else 0
    message_chat = 1 if 'message' in data_dict else 0
    
    if username and create_server_name and game:

        pass
    else:
        raise HTTPException(status_code=403, detail="Add Username, Server Name and Game to create a server.")
        pass
    
@router.post('/jserver_form')
async def read_root(request: Request):
    form_data = await request.form()
    data_dict = dict(form_data)
    username = data_dict['username']
    join_server_name = data_dict['join_server_name']
    
    if username and join_server_name:
        pass
    