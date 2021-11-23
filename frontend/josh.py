import asyncio
import os
from time import time

from dotenv import load_dotenv
from playsound import playsound

from treekit.lighting_client import LightingClient
from treekit import sarajevo

client = LightingClient(400)
pixels = client.pixels

async def main():
    await client.connect(os.getenv('ADDRESS', 'localhost:8000'))

    playsound('music/christmas.mp3', block=False)
    start_time = last_update = time()
    timecode = 0

    while timecode < 221:
        pixels[:] = (0, 0, 0)

        if 0 <= timecode < 38:
            sarajevo.intro(pixels, timecode)
        elif 38.7 <= timecode < 39:
            sarajevo.flash(pixels)
        elif 39 <= timecode < 50.5:
            sarajevo.twinkle(pixels)
        elif 50.5 <= timecode < 51:
            sarajevo.flash(pixels)
        elif 51 <= timecode < 58:
            sarajevo.twinkle(pixels)
        elif 58 <= timecode < 58.5:
            sarajevo.flash(pixels)
        elif 58.5 <= timecode < 62:
            sarajevo.twinkle(pixels)

        await client.send_frame()
        last_update = time()

        current_time = time()
        if current_time - last_update < 0.05:
            await asyncio.sleep(0.05 - (current_time - last_update))

        timecode = time() - start_time


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        asyncio.get_event_loop().run_until_complete(client.close())
        asyncio.get_event_loop().run_forever()
    finally:
        asyncio.get_event_loop().close()
