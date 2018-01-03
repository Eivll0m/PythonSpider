## 开发环境
* Windows 7
* Python 2.7.10
* Pycharm 2017
* Scrapy 1.5.0

## 安装Scrapy
```bash
pip install Scrapy
```
## 运行爬虫
 
```bash
cd hshfy
scrapy crawl Myhshfy
```
## 更新记录
**2018年01月03日新增代理功能**
* middlewares.py新增类：

```python
class ProxyMiddleWare(object):
    """docstring for ProxyMiddleWare"""

    def process_request(self, request, spider):
        '''对request对象加上proxy'''
        proxy = self.get_random_proxy()
        print "this is request ip:" + proxy
        request.meta['proxy'] = proxy

    def process_response(self, request, response, spider):
        '''对返回的response处理'''
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            proxy = self.get_random_proxy()
            print "this is response ip:" + proxy
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            return request
        return response

    def get_random_proxy(self):
        '''随机从文件中读取proxy'''
        while 1:
            with open('E:\Code\Py-Pj\hshfy\hshfy\proxies.txt', 'r') as f:
                proxies = f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy = random.choice(proxies).strip()
        return proxy
```

* settings.py配置更新:

```python
DOWNLOADER_MIDDLEWARES = {
    'hshfy.middlewares.HshfyDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,
    'hshfy.middlewares.RotateUserAgentMiddleware':400,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware':None,
    'hshfy.middlewares.ProxyMiddleWare':125,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware':None,
}
```
