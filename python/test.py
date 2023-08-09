import socketio

sio = socketio.Client()

@sio.event
def connect():
    sio.emit("ID", 'steph-pi')
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.2.13:3000')
sio.wait()