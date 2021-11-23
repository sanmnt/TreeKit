import asyncio
import os
import random
from dotenv import load_dotenv
from treekit.lighting_client import LightingClient

load_dotenv()

async def main():
    client = LightingClient(400)
    pixels = client.pixels
    await client.connect(os.getenv('ADDRESS', 'localhost:8000'))
    pixels[:] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    await client.send_frame()


def showing():
    asyncio.get_event_loop().run_until_complete(main())

if __name__ == '__main__':
    showing()
