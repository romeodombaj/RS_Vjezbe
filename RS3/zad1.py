import asyncio

async def korutina():
    print("početak dohvaćanja")
    podaci = list(range(1,11))
    await asyncio.sleep(3)
    print("podaci dohvaćeni:\n", podaci)
    return podaci

asyncio.run(korutina())

    
