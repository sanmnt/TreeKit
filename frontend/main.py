import asyncio
from treekit.lighting_client import LightingClient


async def main():
    client = LightingClient(120)
    pixels = client.pixels

    await client.connect('localhost:8000')

    pixels[0] = (128,0,0)
    await client.send_frame()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
