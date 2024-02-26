import asyncio
import aiohttp
from aiohttp import TCPConnector, ClientTimeout

async def fetch_data(url, timeout):
    print(f"Start fetching data from {url}")
    connector = TCPConnector(ssl=False)  # 不验证 SSL 证书
    async with aiohttp.ClientSession(connector=connector) as session:
        try:
            timeout_obj = ClientTimeout(total=timeout)
            async with session.get(url, timeout=timeout_obj) as response:
                print(response.status)
                data = await response.text()
                print(f"Data fetched from {url}")
        except asyncio.TimeoutError:
            print(f"Timeout occurred while fetching data from {url}")

async def main():
    # 创建任务列表
    urls = [
        "http://137.175.50.117:5700",
        "https://www.baidu.com",
        "https://cn.bing.com/",
        # 添加更多的 URL
    ]

    tasks = [fetch_data(url, timeout=5) for url in urls]
    # 并发执行协程任务
    await asyncio.gather(*tasks)

# 运行主协程
asyncio.run(main())
