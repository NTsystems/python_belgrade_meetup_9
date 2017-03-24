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
            models.add_tweet(data)
            count = models.get_counts()
            if clients and data.get('hashtags', []):
                clients[0].send_message({'tweet': data, 'count': count})
            self.write({'status': "ok"})
        except:
            self.write({'status': "error"})

    def get(self):
        try:
            hashtag = self.get_argument("hashtag", "")
            tweets = models.get_last_tweets(hashtag)
            self.write(tweets)
        except:
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
