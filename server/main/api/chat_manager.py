# # -*- coding: utf-8 -*-
#
#
# import gevent
# import redis
#
# class CHANNEL:
#     CHAT      = 'chat'
#
# CHANNELS = [
#     CHANNEL.CHAT,
# ]
#
# class Subscribers(object):
#     def __init__(self):
#         self.clients = {}
#         self.redis = redis.StrictRedis('127.0.0.1', port='6379', decode_responses=True)
#         self.pubsub = self.redis.pubsub()
#         for c in CHANNELS:
#             self.pubsub.subscribe(c)
#
#     def __iter_message(self):
#         for message in self.pubsub.listen():
#             data = message.get('data')
#             if message['type'] == 'message':
#                 yield message
#
#     def register(self, client, channel):
#         """Register a WebSocket connection for Redis updates."""
#         if self.clients.get(channel, None) is None:
#             self.clients[channel] = set()
#         self.clients[channel].add(client)
#
#     def publish(self, channel, message):
#         print(channel, message)
#         self.redis.publish(channel, message)
#
#     def send(self, client, channel, data):
#         """Send given data to the registered client.
#         Automatically discards invalid connections."""
#         try:
#             client.send(data)
#         except Exception:
#             self.clients[channel].remove(client)
#
#     def run(self):
#         """Listens for new messages in Redis, and sends them to clients."""
#         for message in self.__iter_message():
#             channel = message.get('channel', '')
#             for client in self.clients.get(channel, set()):
#                 gevent.spawn(self.send, client, channel, message.get('data'))
#
#     def start(self):
#         """Maintains Redis subscription in the background."""
#         gevent.spawn(self.run)
#
# SUBSCRIBER = Subscribers()
# SUBSCRIBER.start()