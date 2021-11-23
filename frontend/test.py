import asyncio
import os

from dotenv import load_dotenv
from treekit.lighting_client import LightingClient

async def main():
    client = LightingClient(400)
    pixels = client.pixels

    await client.connect('10.10.0.167:8000')

    while True:
        pixels[:] = (128, 0, 0)
        await client.send_frame()
        await asyncio.sleep(1)

        pixels[:] = (0, 128, 0)
        await client.send_frame()
        await asyncio.sleep(1)

        pixels[:] = (0, 0, 128)
        await client.send_frame()
        await asyncio.sleep(1)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
