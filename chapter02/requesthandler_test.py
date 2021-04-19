from tornado.web import RequestHandler
import json


class MainHandler(RequestHandler):
    # 入口
    # def initialize(self, db):
    #     # 用于初始化handler类的过程
    #     self.db = db

    def prepare(self):
        # 用户真正调用请求处理之前的初始化方法
        # 1. 打印日志， 打开文件等
        pass

    def on_finish(self) -> None:
        # 请求结束后调用
        # 关闭句柄，清理内存
        pass

    # http方法
    def get(self, *args, **kwargs):
        # data1 = self.get_query_argument("name")    str    只能获取get方法值
        # data2 = self.get_query_arguments("name")    list   只能获取get方法值

        # data1 = self.get_argument("name")   # str    可以获取post方法值
        # data2 = self.get_arguments("name")  # list   可以获取post方法值

        # 当前端发送json数据时
        param = self.request.body.decode("utf8")
        data1 = json.loads(param)
        pass

    def post(self, *args, **kwargs):
        try:
            data1 = self.get_body_argument("name")
            data2 = self.get_body_arguments("name")
        except Exception as e:
            self.set_status(500)
            # self.finish() 断开连接
            # self.finish({"name": "boodf"})
            # self.redirect()  跳转页面  self.redirect("", permanent=True) True 返回301    False 返回302
            # 301是永久重定向   302是临时重定向
            # self.write()   可以写多个   返回前端不换行

    def write_error(self, status_code, **kwargs):
        # 错误的时候使用
        pass


if __name__ == '__main__':
    from tornado import web, ioloop

    app = web.Application([
        ("/", MainHandler)
    ], debug=True)
    app.listen(8888)
    ioloop.IOLoop.current().start()
