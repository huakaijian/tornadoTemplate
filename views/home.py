from abc import ABC

from tornado.web import RequestHandler


class HomeHandler(RequestHandler, ABC):
    """主路由处理类"""

    def get(self):
        """对应http的get请求方式"""
        self.write("this is home pager")
