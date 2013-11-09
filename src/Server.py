import os
import tornado.web
from tornado.web import StaticFileHandler
import Mojifi


def abs_path(filename):
    return os.path.join(os.getcwd(), filename)


class MainHandler(tornado.web.RequestHandler):
    """docstring for MainHandler"""
    def initialize(self, **kwargs):
        self.__dict__.update(kwargs)

    def get(self, *args):
        self.render(
            #TODO: Define template_path properly
            "html/main.html",
            text=' '.join(self.translator.translate(' '.join(args))))


######################################################################


def main():
    d = Mojifi.SymbolDictionary("dicts/emoji-mdown.json", None)
    t = Mojifi.Translator(d)

    settings = dict(
        # template_path="html/",
        debug=True)

    application = tornado.web.Application([
        (r"/js/(.*)", StaticFileHandler, {'path': 'js/'}),
        (r"/css/(.*)", StaticFileHandler, {'path': 'css/'}),
        (r"/(.*)", MainHandler, dict(translator=t))
    ], settings)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
