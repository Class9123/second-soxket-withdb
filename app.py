
from flask import Flask, render_template_string
from flask_cors import CORS
from flask_socketio import SocketIO as sio

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app)
socket=sio(app ,cors_allowed_origins="*")

# HTML content as a string
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask-SocketIO Example</title>
    <script src="https://cdn.socket.io/4.0.1/socket.io.min.js"></script>
    <script type="text/javascript">
        var socket = io();
        
        socket.on('connect', function() {
            console.log('Connected to server');
        });
        
        socket.on('response', function(data) {
            console.log('Received response: ' + data);
            // Display response on the webpage
            document.getElementById('messages').innerHTML += '<li>' + data + '</li>';
        });
        
        function sendMessage() {
            var message = document.getElementById('message_input').value;
            console.log('Sending message: ' + message);
            socket.emit('message', message);
            document.getElementById('message_input').value = '';
        }
    </script>
</head>
<body>
    <h1>Flask-SocketIO jcxftsufyfExample</h1>
    <input type="text" id="message_input" placeholder="Type your message...">
    <button onclick="sendMessage()">Send</button>
    <ul id="messages"></ul>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(html_content)


if __name__ == '__main__':
    app.run( debug=True)
    
