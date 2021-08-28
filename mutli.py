from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import threading
import os
import time


def work(n):
    print(f'给{n}打电话,进程号：{os.getpid()}，线程号：{threading.current_thread()}')
    time. sleep(3)
    print(f"{n}通话结束,进程号：{os.getpid()}，线程号：{threading.current_thread()}")
userlist= ["刘德华",'吴彦祖','梁朝伟','周杰伦','林俊杰']

#1. 创建线程池，推荐
pool = ThreadPoolExecutor(max_workers = 3)
#1. 创建进程池
# pool = ProcessPoolExecutor(max_workers = 3)


#2. 指派任务,指定对应任务和参数
# [pool.submit(work,user) for user in userlist]

#3. 关闭
pool.shutdwon()


import time
def wait_on_b():
    time.sleep(5)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5

def wait_on_a():
    time.sleep(5)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


executor = ThreadPoolExecutor(max_workers=2)
a = executor.submit(wait_on_b)
b = executor.submit(wait_on_a)

a.result()
import concurrent.futures
import urllib.request

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
