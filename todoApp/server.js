const express = require('express')
const app = express()
const server = require('http').createServer(app);
const WebSocket = require('ws');
const wss = new WebSocket.Server({server:server});
var data;

wss.on('connection', function connection(ws) {
  console.log('New client connected!');
  ws.on('message', function incoming(message) {
    data = JSON.parse(message);
    if (data.gap < 0) {
      ws.send("Emergency: your task \'" + data.name + "\' is " + data.gap + " days late.");
    }
    else {
      ws.send("Warning: " + data.gap + " days left to complete your task \'" + data.name + "\'.");
    }
  });
});

app.get('/', (req, res) => {
  res.send('Hello World!')
})
server.listen(3000, () => console.log('Listening on port : 3000'))