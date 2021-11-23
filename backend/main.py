import asyncio
import os

from dotenv import load_dotenv
from neopixel_plus import NeoPixel
from websockets import serve
from websockets.connection import State

load_dotenv()
PIXEL_COUNT = os.getenv('PIN', 400)
pixel = NeoPixel(
                  n=PIXEL_COUNT,
                  pin_num=os.getenv('PIN', 18),
                  test=bool(os.getenv('TEST', False)),
                  target='adafruit'
                )

def __unpack_frame(frame):
    data = []
    for i in range(0, len(frame), 3):
        data.append(list(frame[i:i + 3]))

    return data

async def handler(websocket, path):
    while websocket.state == State.OPEN:
        frame = await websocket.recv()
        if len(frame) != PIXEL_COUNT * 3:
            print('Frame size != PIXEL_COUNT')
            return

        data = __unpack_frame(frame)
        pixel.leds[:] = data
        pixel.write()

async def main():
    async with serve(handler, "0.0.0.0", 8000, ping_interval=None):
        print('Server up!')
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
