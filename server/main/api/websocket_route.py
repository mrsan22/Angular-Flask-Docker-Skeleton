# -*- coding: utf-8 -*-

from server.main import socketio


@socketio.on('my event', namespace='/websocket_test')
def my_event(msg):
    print(msg)

@socketio.on('my_ping', namespace='/websocket_test')
def ping_pong():
    socketio.emit('my_pong')

@socketio.on('my broadcast event', namespace='/websocket_test')
def test_message(message):
    socketio.emit('my response', {'data': message['data']}, broadcast=True)


@socketio.on('message', namespace='/websocket_test')
def chat_message(message):
    socketio.emit('message', {'data': message['data']}, broadcast = True)

@socketio.on('connect', namespace='/websocket_test')
def test_connect():
    socketio.emit('my response', {'data': 'Connected', 'count': 0})

@socketio.on('disconnect', namespace='/websocket_test')
def test_disconnect():
    print('Client disconnected')