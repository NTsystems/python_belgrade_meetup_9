import tornado.ioloop
import tornado.web
import models
from tornado import websocket
import json
import os

clients = []
root = os.path.dirname(__file__)


class Tweets(tornado.web.RequestHandler):
    def post(self):

        try:
            data = json.loads(self.request.body.decode('utf-8'))
            models.addTweet(data)
            count = models.getCounts()
            if clients and data.get('hashtags', []):
                clients[0].send_message({'tweet': data, 'count': count})
            self.write({'status': "ok"})
        except Exception as e:
            print(str(e))
            self.write()

    def get(self):
        try:
            print('get hashtags')
            hashtag = self.get_argument("hashtag", "")
            print(hashtag)
            tweets = models.getLastTweets(hashtag)
            self.write(tweets)
        except Exception as e:
            print(str(e))
            pass


class SocketHandler(websocket.WebSocketHandler):
    def check_origin(self, origin):
        print(origin)
        return True

    def open(self):
        print('open')
        if self not in clients:
            clients.append(self)

    def on_close(self):
        if self in clients:
            clients.remove(self)

    def on_message(self, message):
        pass

    @staticmethod
    def send_message(data):
        for client in clients:
            client.write_message(data)


def make_app():
    return tornado.web.Application([
        (r"/tweets/?", Tweets),
        (r'/socket/?', SocketHandler),
        (r"/(.*)", tornado.web.StaticFileHandler, {"path": root, "default_filename": "index.html"}),
    ], autoreload=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
