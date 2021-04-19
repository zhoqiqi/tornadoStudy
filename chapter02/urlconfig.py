from tornado import web
import tornado


class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello world6")


class PeopleIdHandler(web.RequestHandler):
    def initialize(self, name):
        self.db_name = name

    async def get(self, id, *args, **kwargs):
        self.write(f"db_name: {self.db_name}")
        # 如何使用name
        # self.write(self.reverse_url("people_name", "zhouqiqi"))
        # 跳转
        # self.redirect(self.reverse_url("people_name", "zhouqiqi"))


class PeopleNameHandler(web.RequestHandler):
    async def get(self, name, *args, **kwargs):
        self.write(f"用户姓名: {name}")


class PeopleInfoHandler(web.RequestHandler):
    async def get(self, name, age, gender, *args, **kwargs):
        self.write(f"用户姓名: {name},年龄: {age}, 性别: {gender}")


# 通过url 初始化一些参数
people_db = {
    "name": "people"
}

# 配置如/people/1/
urls = [
    tornado.web.URLSpec("/", MainHandler, name="index"),
    tornado.web.URLSpec(r"/people/(\d+)/?", PeopleIdHandler, people_db, name="people_id"),
    tornado.web.URLSpec(r"/people/(\w+)/", PeopleNameHandler, name="people_named"),
    (r"/people/(?P<name>\w+)/(?P<age>\d+)/(?P<gender>\w+)/", PeopleInfoHandler)  # 推荐
]

if __name__ == '__main__':
    app = web.Application(urls, debug=True)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

# 知识点
# 1.url的各种参数的配置
