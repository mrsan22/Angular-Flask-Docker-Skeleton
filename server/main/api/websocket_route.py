# -*- coding: utf-8 -*-

from server.main import socketio
from flask import request
from flask_socketio import emit

count = 0

# @socketio.on('my-message', namespace='/websocket_test')
# def msg(message):
#     msg = message['data']['content']
#     # Only emitting to sender by using its sid
#     emit('message', msg, room=request.sid)

@socketio.on('json', namespace='/websocket_test')
def chat_message(message):
    broadcast = message['data']['isBroadcast']
    emit('my response', {'data': message['data']['content']}, broadcast = broadcast)

@socketio.on('connect', namespace='/websocket_test')
def test_connect():
    global count
    count  += 1
    emit('my response', {'data': 'Connected', 'count': count}, broadcast=True)

@socketio.on('disconnect', namespace='/websocket_test')
def test_disconnect():
    global count
    count -= 1
    emit('my response', {'data': 'Connected', 'count': count}, broadcast=True)