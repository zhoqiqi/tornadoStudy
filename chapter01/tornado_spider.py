from tornado import gen, httpclient, ioloop, queues
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "http://www.tornadoweb.org/en/stable/"
concurrency = 3


async def get_url_links(url):
    response = await httpclient.AsyncHTTPClient().fetch(base_url)
    html = response.body.decode("utf8")
    soup = BeautifulSoup(html)
    links = [urljoin(base_url, a.get("href")) for a in soup.find_all("a", href=True)]
    return links


async def main():
    seen_set = set()
    q = queues.Queue()

    async def fetch_url(current_url):
        # 生产者
        if current_url in seen_set:
            return
        print(f"获取: {current_url}")
        seen_set.add(current_url)
        next_urls = await get_url_links(current_url)
        for new_url in next_urls:
            if new_url.startswith(base_url):
                # 放入队列, 使用await 是为了当这个协程放不进去的时候切换出来，切换到另一个get()协程上
                await q.put(new_url)

    async def worker():
        async for url in q:
            if url is None:
                return
            try:
                await fetch_url(url)
            except Exception as e:
                print("Exception")
            finally:
                # 将数据减一  消费了一个
                q.task_done()

    await q.put(base_url)
    workers = gen.multi([worker() for _ in range(concurrency)])
    await q.join()
    for _ in range(concurrency):
        await q.put(None)
    await workers


if __name__ == "__main__":
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(main)
