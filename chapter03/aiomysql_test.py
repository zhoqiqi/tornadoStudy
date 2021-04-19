import asyncio
from aiomysql import create_pool
from tornado import ioloop


async def go():
    async with create_pool(host='127.0.0.1', port=3306, user='root', password='123456', db='message',
                           charset="utf8") as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute("select * from message")
                value = await cur.fetchone()
                print(value)


if __name__ == '__main__':
    # 运行方法一    异步方法要用协程方法运行
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(go())

    # 方法二
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(go)
