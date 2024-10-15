console.log("Hello World")
let ws = require('ws')
let server = new ws.Server({ port:'3000'})

server.on('connection', socket => {
    socket.on('message', message =>{
       socket.send(`${message}`)
       console.log(message)
    })
});