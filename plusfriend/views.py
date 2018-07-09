from .decorators import bot
from . import functions


@bot
def on_init(request):
    return {'type': 'text'}


@bot
def on_message(request):
    user_key = request.JSON['user_key']
    type = request.JSON['type']
    content = request.JSON['content']  # photo 타입일 경우에는 이미지 URL
    response = '아직 구현되지 않았습니다'
    
    return {
        'message': {
            'text': response,
        }
    }


@bot
def on_added(request):
    user_key = request.JSON['user_key']

@bot
def on_block(request, user_key):
    pass

@bot
def on_leave(request, user_key):
    pass
