import asyncio
async def main():
    print('pawat')
    await foo('text')
    print('finished')

async def foo(text):
    print(text)
    await asyncio.sleep(5)
asyncio.run(main())
