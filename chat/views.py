from django.shortcuts import render
import socketio

from .models import Message
from .forms import MessageForm

sio = socketio.Server(async_mode=None)

def index(request):
    context = {}
    context["message_list"] = Message.objects.all()
    context["form"] = MessageForm(request.POST or None)

    return render(request, "chat/index.html", context)

@sio.event
def new_chat(sid, message):
    content = message["data"]
    message = Message(content=content)
    message.save()

    sio.emit("get_new_chat", {"data": content})