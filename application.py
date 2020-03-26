import tornado.web

from config import settings
from views.home import HomeHandler
from views.index import IndexHandler


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/home", HomeHandler),

        ]
        super().__init__(handlers, **settings)
