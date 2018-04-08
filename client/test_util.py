from client.py_cli import ProxyFetcher

args = dict(host='127.0.0.1', port=6379, password='', db=0)
fetcher = ProxyFetcher('zhihu', strategy='greedy', redis_args=args)
# 获取一个可用代理
# print(fetcher.get_proxy())
# 获取可用代理列表
print(fetcher.get_proxies()) # or print(fetcher.pool)
print(fetcher.get_proxies().__sizeof__())