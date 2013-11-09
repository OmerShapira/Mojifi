import os
import tornado.web
from tornado.web import StaticFileHandler
from tornado.options import define, options
from tornado.log import logging

import Mojifi

######################################################################

def abs_path(filename):
    return os.path.join(os.getcwd(), filename)


class MainHandler(tornado.web.RequestHandler):
    """docstring for MainHandler"""
    def initialize(self, **kwargs):
        self.__dict__.update(kwargs)

    def get(self, *args):
        self.render(
            "main.html",
            text=' '.join(self.translator.translate(' '.join(args))))


######################################################################

define("port", default=8888, help="run on the given port", type=int)
dict_path = "dicts/emoji-mdown.json"

######################################################################


def main():
    # TODO : Prettify this code
    logging.info("Loading Dictionary from: {}".format(dict_path))
    d = Mojifi.SymbolDictionary(dict_path, None)
    t = Mojifi.Translator(d)

    # Server Config
    settings = dict(
        template_path="html/",
        debug=True)

    server_settings = dict(
        xheaders=True)

    tornado.options.parse_command_line()

    # Server Startup
    logging.info("Running Tornado at http://localhost:%s" % options.port)
    application = tornado.web.Application([
        (r"/js/(.*)", StaticFileHandler, {'path': 'js/'}),
        (r"/css/(.*)", StaticFileHandler, {'path': 'css/'}),
        (r"/(.*)", MainHandler, dict(translator=t))],
        **settings)

    application.listen(options.port, **server_settings)

    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
