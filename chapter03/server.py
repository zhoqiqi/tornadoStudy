from tornado.web import RequestHandler, StaticFileHandler
from tornado import web, ioloop
from aiomysql import create_pool


class MainHandler(RequestHandler):
    def initialize(self, db):
        self.db = db

    async def get(self, *args, **kwargs):
        id = ""
        name = ""
        email = ""
        address = ""
        message = ""
        async with create_pool(host='127.0.0.1', port=3306, user='root', password='123456', db='message',
                               charset="utf8") as pool:
            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    await cur.execute("select * from message")
                    value = await cur.fetchone()
                    id, name, email, address, message = value
        self.render("message.html", id=id, name=name, email=email, address=address, message=message)


settings = {
    "static_path": "/home/zhouqiqi/Desktop/python_test/tornadoTest/tornadoStudy/chapter03/static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
    "db": {
        "host": "127.0.0.1",
        "user": "root",
        "password": "123456",
        "name": "message",
        "port": 3306,
        "charset": "utf8"
    }
}

if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler, {"db": settings["db"]}),
        (r"/static/(.*)", StaticFileHandler,
         {"path": "/home/zhouqiqi/Desktop/python_test/tornadoTest/tornadoStudy/chapter03/static"})
    ], debug=True, **settings)
    app.listen(8888)
    ioloop.IOLoop.current().start()
