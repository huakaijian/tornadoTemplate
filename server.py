
import tornado
import config
from application import Application

if __name__ == "__main__":
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(config.options["port"])
    tornado.ioloop.IOLoop.current().start()
