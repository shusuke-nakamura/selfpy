import asyncio
import time


async def heavey_process(name, sec):
    print(f'start {name}')
    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'{name}/{sec}'


# async def main():
#     print(await heavey_process('hoge', 2))
#     print(await heavey_process('bar', 5))
#     print(await heavey_process('piyo', 1))

async def main():
    t1 = asyncio.create_task(heavey_process('hoge', 2))
    t2 = asyncio.create_task(heavey_process('bar', 5))
    t3 = asyncio.create_task(heavey_process('piyo', 1))
    print(await t1)
    print(await t2)
    print(await t3)


start = time.time()
loop = asyncio.get_event_loop()
asyncio.run(main())
end = time.time()
print(f'Process Time: {end - start}')
