from client.py_cli import ProxyFetcher

args = dict(host='127.0.0.1', port=6379, password='', db=0)
fetcher = ProxyFetcher('zhihu', strategy='greedy', redis_args=args)
# ��ȡһ�����ô���
# print(fetcher.get_proxy())
# ��ȡ���ô����б�
print(fetcher.get_proxies()) # or print(fetcher.pool)
print(fetcher.get_proxies().__sizeof__())