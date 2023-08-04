const io = require('socket.io-client')
const socket = io.connect('http://192.168.2.14:3000', { reconnect: true });

socket.on('connect', function () {
    console.log("socket connected"); 
});

socket.on('broadcast', function (data) {
    console.log("we got a broadcast: ", data);
});