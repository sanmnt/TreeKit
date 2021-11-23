import asyncio
import os
import time
from random import randint

from dotenv import load_dotenv
from treekit.lighting_client import LightingClient

PIXEL_NUM = 400

client = LightingClient(PIXEL_NUM)
pixel = client.pixels


async def main():
    await client.connect(os.getenv('ADDRESS', 'localhost:8000'))

    while True:
        r = randint(0,255)
        b = randint(0,255)
        g = randint(0,255)
       # p = randint(0,399)
       # print(f"{p}: {r},{g},{b}")
       # pixel[int(p)] = (r,b,g)
       # await asyncio.sleep(.02)
        #print(f"{p}: {r},{g},{b}")
        rr =255
        gg = 0
        for i in range(15):
            for v in range(0,399):
                pixel[v]= (rr,gg,0)
            await asyncio.sleep(.1)
            await client.send_frame()
            for v in range(0,399):
                pixel[v] = (0,0,0)
            await asyncio.sleep(.1)
            await client.send_frame()
            if (i % 2) == 0:
                rr = 0
                gg = 255
            else:
                rr= 255
                gg= 0
        for i in range(1):
            for v in range(0,399):
                pixel[v] = (255,255,255)
                await asyncio.sleep(0.001)
                await client.send_frame()
            for v in range(399,0,-1):
                pixel[v] = (0,0,0)
                await asyncio.sleep(0.001)
                await client.send_frame()
           # await asyncio.sleep(1)
            await client.send_frame()
        for v in range(0,399):
            r = randint(140,255)
            g = randint(0,100)
            b = randint(0,255)
            pixel[v] =(r,g,b)
        await client.send_frame()
        await asyncio.sleep(4)
        await client.send_frame()
        rr= 255
        gg = 0
        for i in range(15):
            for v in range(0,399):
                pixel[v] = (rr,gg,0)
            await asyncio.sleep(.1)
            await client.send_frame()
            for v in range(0,399):
                pixel[v] = (0,0,0)
            await asyncio.sleep(.1)
            await client.send_frame()
            if (i% 2) == 0:
                rr= 0
                gg = 255
            else:
                rr= 255
                gg=0
       # for v in range(0,399):
        #    pixel[v] = (255,0,0)
       # await client.send_frame()
       # await asyncio.sleep(3)
       # await client.send_frame()
      # for x in range(15):
        count = 0
        rrr = 255
        ggg = 0
        countz = 0
        countw = 0
        for x in range(60):
            if (countz%2 == 0):
                count = 10
                countz = countz +1
            else:
                count = 0
                countz= countz +1
            for v in range(0,399):
                if count == 10:
                    if (countw%2) == 0:
                        rrr =  0
                        ggg = 255
                        countw = countw + 1
                        count = 0
                    elif (countw%2) != 0:
                        rrr= 255
                        ggg= 0
                        count= 0
                        countw= countw+1
                pixel[v] = (rrr,ggg,0)
                count = count + 1
            await client.send_frame()
            await asyncio.sleep(.5)

if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        asyncio.get_event_loop().run_until_complete(client.close())
        asyncio.get_event_loop().run_forever()
    finally:
        asyncio.get_event_loop().close()
