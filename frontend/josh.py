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
            sarajevo.fade_out(pixels, timecode, (255, 255, 255), 38.7, 39)
        elif 39 <= timecode < 50.5:
            sarajevo.twinkle(pixels)
        elif 50.5 <= timecode < 51:
            sarajevo.fade_out(pixels, timecode, (255, 255, 255), 50.5, 51)
        elif 51 <= timecode < 58:
            sarajevo.twinkle(pixels)
        elif 58 <= timecode < 58.5:
            sarajevo.fade_out(pixels, timecode, (255, 255, 255), 58, 58.5)
        elif 58.5 <= timecode < 62:
            sarajevo.twinkle(pixels)

        elif 62 <= timecode < 62.2:
            sarajevo.tumble_up(pixels, 1, ('r'))
        elif 62.2 <= timecode < 62.4:
            sarajevo.tumble_up(pixels, 2, ('r'))
        elif 62.4 <= timecode < 62.6:
            sarajevo.tumble_up(pixels, 3, ('r'))
        elif 62.6 <= timecode < 62.8:
            sarajevo.tumble_up(pixels, 4, ('r'))
        elif 62.8 <= timecode < 63:
            sarajevo.tumble_up(pixels, 5, ('r'))
        elif 63 <= timecode < 63.2:
            sarajevo.tumble_up(pixels, 1, ('g'))
        elif 63.2 <= timecode < 63.4:
            sarajevo.tumble_up(pixels, 2, ('g'))
        elif 63.4 <= timecode < 63.6:
            sarajevo.tumble_up(pixels, 3, ('g'))
        elif 63.6 <= timecode < 63.8:
            sarajevo.tumble_up(pixels, 4, ('g'))
        elif 63.8 <= timecode < 64:
            sarajevo.tumble_up(pixels, 5, ('g'))
        elif 64 <= timecode < 64.2:
            sarajevo.tumble_up(pixels, 1, ('b'))
        elif 64.2 <= timecode < 64.4:
            sarajevo.tumble_up(pixels, 2, ('b'))
        elif 64.4 <= timecode < 64.6:
            sarajevo.tumble_up(pixels, 3, ('b'))
        elif 64.6 <= timecode < 64.8:
            sarajevo.tumble_up(pixels, 4, ('b'))
        elif 64.8 <= timecode < 65:
            sarajevo.tumble_up(pixels, 5, ('b'))
        elif 65 <= timecode < 65.2:
            sarajevo.tumble_up(pixels, 1, ('', 'r'))
        elif 65.2 <= timecode < 65.4:
            sarajevo.tumble_up(pixels, 2, ('', 'r'))
        elif 65.4 <= timecode < 65.6:
            sarajevo.tumble_up(pixels, 3, ('', 'r'))
        elif 65.6 <= timecode < 65.8:
            sarajevo.tumble_up(pixels, 4, ('', 'r'))
        elif 65.8 <= timecode < 66:
            sarajevo.tumble_up(pixels, 5, ('', 'r'))

        elif 66 <= timecode < 66.2:
            sarajevo.tumble_up(pixels, 1, ('r', '', 'g'))
        elif 66.2 <= timecode < 66.4:
            sarajevo.tumble_up(pixels, 2, ('r', '', 'g'))
        elif 66.4 <= timecode < 66.6:
            sarajevo.tumble_up(pixels, 3, ('r', '', 'g'))
        elif 66.6 <= timecode < 66.8:
            sarajevo.tumble_up(pixels, 4, ('r', '', 'g'))
        elif 66.8 <= timecode < 67:
            sarajevo.tumble_up(pixels, 5, ('r', '', 'g'))
        elif 67 <= timecode < 67.2:
            sarajevo.tumble_up(pixels, 1, ('r', '', 'b'))
        elif 67.2 <= timecode < 67.4:
            sarajevo.tumble_up(pixels, 2, ('r', '', 'b'))
        elif 67.4 <= timecode < 67.6:
            sarajevo.tumble_up(pixels, 3, ('r', '', 'b'))
        elif 67.6 <= timecode < 67.8:
            sarajevo.tumble_up(pixels, 4, ('r', '', 'b'))
        elif 67.8 <= timecode < 68:
            sarajevo.tumble_up(pixels, 5, ('r', '', 'b'))
        elif 68 <= timecode < 68.2:
            sarajevo.tumble_up(pixels, 1, ('b', '', 'g'))
        elif 68.2 <= timecode < 68.4:
            sarajevo.tumble_up(pixels, 2, ('b', '', 'g'))
        elif 68.4 <= timecode < 68.6:
            sarajevo.tumble_up(pixels, 3, ('b', '', 'g'))
        elif 68.6 <= timecode < 68.8:
            sarajevo.tumble_up(pixels, 4, ('b', '', 'g'))
        elif 68.8 <= timecode < 69:
            sarajevo.tumble_up(pixels, 5, ('b', '', 'g'))
        elif 69 <= timecode < 69.2:
            sarajevo.tumble_up(pixels, 1, ('b', '', 'r'))
        elif 69.2 <= timecode < 69.4:
            sarajevo.tumble_up(pixels, 2, ('b', '', 'r'))
        elif 69.4 <= timecode < 69.6:
            sarajevo.tumble_up(pixels, 3, ('b', '', 'r'))
        elif 69.6 <= timecode < 69.8:
            sarajevo.tumble_up(pixels, 4, ('b', '', 'r'))
        elif 69.8 <= timecode < 70:
            sarajevo.tumble_up(pixels, 5, ('b', '', 'r'))

        elif 70 <= timecode < 70.2:
            sarajevo.tumble_up(pixels, 1, ('b', 'r', 'g'))
        elif 70.2 <= timecode < 70.4:
            sarajevo.tumble_up(pixels, 2, ('b', 'r', 'g'))
        elif 70.4 <= timecode < 70.6:
            sarajevo.tumble_up(pixels, 3, ('b', 'r', 'g'))
        elif 70.6 <= timecode < 70.8:
            sarajevo.tumble_up(pixels, 4, ('b', 'r', 'g'))
        elif 70.8 <= timecode < 71:
            sarajevo.tumble_up(pixels, 5, ('b', 'r', 'g'))
        elif 71 <= timecode < 71.2:
            sarajevo.tumble_up(pixels, 1, ('g', 'r', 'b'))
        elif 71.2 <= timecode < 71.4:
            sarajevo.tumble_up(pixels, 2, ('g', 'r', 'b'))
        elif 71.4 <= timecode < 71.6:
            sarajevo.tumble_up(pixels, 3, ('g', 'r', 'b'))
        elif 71.6 <= timecode < 71.8:
            sarajevo.tumble_up(pixels, 4, ('g', 'r', 'b'))
        elif 71.8 <= timecode < 72:
            sarajevo.tumble_up(pixels, 5, ('g', 'r', 'b'))
        elif 72 <= timecode < 72.2:
            sarajevo.tumble_up(pixels, 1, ('r', 'g', 'b'))
        elif 72.2 <= timecode < 72.4:
            sarajevo.tumble_up(pixels, 2, ('r', 'g', 'b'))
        elif 72.4 <= timecode < 72.6:
            sarajevo.tumble_up(pixels, 3, ('r', 'g', 'b'))
        elif 72.6 <= timecode < 72.8:
            sarajevo.tumble_up(pixels, 4, ('r', 'g', 'b'))
        elif 72.8 <= timecode < 73:
            sarajevo.tumble_up(pixels, 5, ('r', 'g', 'b'))

        elif 73 <= timecode < 75:
            sarajevo.follow_up(pixels, timecode, (128, 0, 0), 73, 75)
        elif 75 <= timecode < 77:
            sarajevo.follow_up(pixels, timecode, (0, 128, 0), 75, 77)
        elif 77 <= timecode < 78:
            sarajevo.follow_up(pixels, timecode, (128, 0, 0), 77, 79)
        elif 78 <= timecode < 79:
            sarajevo.follow_up(pixels, timecode, (0, 128, 0), 78, 80)
        elif 79 <= timecode < 81:
            sarajevo.follow_up(pixels, timecode, (0, 0, 128), 79, 81)
        elif 81 <= timecode < 81.2:
            sarajevo.fade_out(pixels, timecode, (255, 255, 255), 81, 81.2)

        elif 81.2 <= timecode < 84.5:
            sarajevo.follow_down(pixels, timecode, (128, 0, 0), 81.2, 84.5)
        elif 84.5 <= timecode < 84.8:
            sarajevo.fade_out(pixels, timecode, (255, 255, 255), 84.5, 84.8)
        elif 84.8 <= timecode < 89:
            sarajevo.follow_down(pixels, timecode, (0, 128, 0), 84.8, 89)
        elif 89 <= timecode < 89.2:
            sarajevo.fade_out(pixels, timecode, (255, 255, 255), 89, 89.2)
        elif 89.2 <= timecode < 92:
            sarajevo.follow_down(pixels, timecode, (0, 0, 128), 89.2, 92)
        elif 92 <= timecode < 92.3:
            sarajevo.follow_down(pixels, timecode, (128, 0, 128), 92, 96)
        elif 92.3 <= timecode < 92.5:
            sarajevo.fade_out(pixels, timecode, (255, 255, 255), 92.3, 92.5)
        elif 92.5 <= timecode < 96:
            sarajevo.follow_down(pixels, timecode, (128, 0, 128), 92, 96)
        elif 96 <= timecode < 100:
            sarajevo.fade_out(pixels, timecode, (255, 255, 255), 96, 100)


        current_time = time()
        if (current_time - last_update) < 0.10:
            await asyncio.sleep(0.10 - (current_time - last_update))

        await client.send_frame()
        last_update = time()
        timecode = time() - start_time


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        asyncio.get_event_loop().run_until_complete(client.close())
        asyncio.get_event_loop().run_forever()
    finally:
        asyncio.get_event_loop().close()
