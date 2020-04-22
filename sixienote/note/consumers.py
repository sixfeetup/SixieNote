import logging
from channels.generic.websocket import AsyncJsonWebsocketConsumer

logger = logging.getLogger(__name__)


class NoteConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("workflow", self.channel_name)
        logger.info(f"Added {self.channel_name} channel to workflow")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("workflow", self.channel_name)
        logger.info(f"Removed {self.channel_name} channel to workflow")

    async def workflow_update(self, event):
        await self.send_json(event)
        logger.info(f"Got message {event} at {self.channel_name}")