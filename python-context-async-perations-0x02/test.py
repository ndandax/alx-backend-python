import asyncio

async def me():
    print("i am starting")
    await asyncio.sleep(5)
    print("I am Ending")
    #print(__file__)

asyncio.run(me())