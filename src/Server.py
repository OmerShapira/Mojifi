import tornado.web
from tornado.web import StaticFileHandler
import Mojifi


class MainHandler(tornado.web.RequestHandler):
    """docstring for MainHandler"""
    def initialize(self, **kwargs):
        self.__dict__.update(kwargs)

    def get(self, *args):
        self.render(
            "html/main.html",
            text=' '.join(self.translator.translate(' '.join(args))))


######################################################################


def main():
    d = Mojifi.SymbolDictionary("/Users/Omer/dev/Mojifi/emoji-mdown.json", None)
    t = Mojifi.Translator(d)

    # settings = dict(
    #     template_path=os.path.join(os.path.dirname(__file__), "templates")

    # settings = dict(js_path="/js/", less_path="/less/")

    application = tornado.web.Application([
        (r"/js/(.*)", StaticFileHandler, {'path': 'js/'}),
        (r"/css/(.*)", StaticFileHandler, {'path': 'css/'}),
        (r"/(.*)", MainHandler, dict(translator=t))
    ], debug=True)
    application.listen(8887)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
