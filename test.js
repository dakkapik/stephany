const { io } = require("socket.io-client");
const socket = io("http://192.168.2.14:3000")

socket.on("connect", ()=> {
    console.log("CONNECTED")
})