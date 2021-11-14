from treekit.pixel_array import PixelArray
import websockets

class LightingClient:
    def __init__(self, num_pixels):
        self.pixels = PixelArray(num_pixels)

    async def connect(self, address):
        self.websocket = await websockets.connect(f'ws://{address}')

    async def send_frame(self):
        await self.websocket.send(self.pixels.bytearr)
