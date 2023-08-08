const {Server} = require("socket.io")
const io = new Server(3000)

io.on("connection", (socket) => {
    console.log("connection")
    socket.on("message", (message)=> {
        console.log(message)
        
    })
})

io.on("message" , (message) => {
  console.log(message)
})