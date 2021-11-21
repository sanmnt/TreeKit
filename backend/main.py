import asyncio
from neopixel_plus import NeoPixel
from websockets import serve

PIXEL_COUNT = 120

pixel = NeoPixel(test=True, n=PIXEL_COUNT)

def __unpack_frame(frame):
    data = []
    for i in range(0, len(frame), 3):
        data.append(list(frame[i:i + 3]))

    return data

async def handler(websocket, path):
    while True:
        frame = await websocket.recv()
        if len(frame) != PIXEL_COUNT * 3:
            print('Frame size != PIXEL_COUNT')
            return

        data = __unpack_frame(frame)
        pixel.leds[:] = data
        pixel.write()

async def main():
    async with serve(handler, "localhost", 8000):
        print('Server up!')
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
