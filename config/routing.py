from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from sixienote.note.consumers import NoteConsumer

application = ProtocolTypeRouter({
    "websocket": URLRouter([
        path("notifications/", NoteConsumer),
    ])
})