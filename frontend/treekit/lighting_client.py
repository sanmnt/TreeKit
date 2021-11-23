import asyncio
from treekit.pixel_array import PixelArray
import websockets

class LightingClient:
    def __init__(self, num_pixels):
        self.pixels = PixelArray(num_pixels)

    async def connect(self, address):
        self.websocket = await websockets.connect(f'ws://{address}', ping_interval=None)

    async def send_frame(self):
        await self.websocket.send(self.pixels.bytearr)

    async def close(self):
        await self.websocket.close()
