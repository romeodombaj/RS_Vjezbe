import asyncio

baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

async def korutina():
    await asyncio.sleep(3)
    print("vraćena baza korisnika")
    return baza_korisnika

async def korutina2():
    await asyncio.sleep(5)
    print("vraćena baza podataka")
    return baza_korisnika


async def main():
    results = await asyncio.gather(asyncio.create_task(korutina()), asyncio.create_task(korutina2()))
    print(results)




asyncio.run(main())

    
