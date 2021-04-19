from tornado.web import StaticFileHandler, RedirectHandler

# 1.RedirectHandler   重定向
# self.redirect 和 RedirectHandler 的区别就是 self.redirect() 是比较灵活的，根据业务逻辑进行临时重定向

from tornado import web
import tornado


class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello world6")


class MainHandler2(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello MainHandler2")


# 可以通过这个获取文件   例：http://172.16.1.128:8888/static/test.png
settings = {
    "static_path": "/home/zhouqiqi/Desktop/python_test/tornadoTest/chapter02/static",
    "static_url_prefix": "/static/"    # 对应设置url中 static   可以修改
}

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler),
        ("/2/", RedirectHandler, {"url": "/"}),
        (r"/static2/(.*)", StaticFileHandler, {"path": "/home/zhouqiqi/Desktop/python_test/tornadoTest/chapter02/static"}),
    ], debug=True, **settings)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
