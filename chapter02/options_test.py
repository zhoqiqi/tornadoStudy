from tornado import web
import tornado
from tornado.options import define, options, parse_command_line

# define   定义一些可以在命令行中传递的参数以及类型
define('port', default=8008, help="run on the given port", type=int)
define('debug', default=True, help="set tornado debug mode", type=bool)

# 使用方法一   运行时手动输入命令从命令行读取   (tornadoEnv) [root@localhost chapter02]# python options_test.py --port=8002
# options.parse_command_line()
# 使用方法二   使用文件定义参数
options.parse_config_file("conf.cfg")


# options 是一个类，全局只有一个options

class MainHandler(web.RequestHandler):
    async def get(self, *args, **kwargs):
        self.write("hello world6")


if __name__ == '__main__':
    app = web.Application([
        ("/", MainHandler)
    ], debug=options.debug)
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

    # 通过这样运行  (tornadoEnv) [root@localhost chapter02]# python options_test.py --port=8002
    # options.port 获取了8002参数
