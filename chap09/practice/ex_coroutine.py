import asyncio
import time


async def heavey_process(name, sec):
    print(f'start {name}')
    await asyncio.sleep(sec)
    print(f'end {name}')
    return f'{name}/{sec}'

start = time.time()
loop = asyncio.get_event_loop()

result = loop.run_until_complete(
    asyncio.gather(
        heavey_process('hoge', 2),
        heavey_process('bar', 5),
        heavey_process('piyo', 1),
        heavey_process('spman', 3)
    )
)

end = time.time()
print(result)
print(f'Process Time: {end - start}')
