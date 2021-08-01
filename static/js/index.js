const sendBtn = document.getElementById('send');
const urlInput = document.getElementById('url');
const responseDiv = document.getElementById('response');
const promptInput = document.getElementById('prompt');

let chatHistory = [];

var socket = io();
socket.on('connect', function() {
    socket.on('response', msg => {
        console.log('response', msg);
        handleResponse(msg.data);
    });
    promptInput.addEventListener('keyup', e => {
        if (e.code === 'Enter') {
            e.preventDefault();
            sendBtn.click();
        }
    });
    sendBtn.addEventListener('click', () => {
        handleSend();
    });
});

function handleSend() {
    sendBtn.disabled = true;
    socket.emit('message', {data: promptInput.value});
}

function handleResponse(response) {
    sendBtn.disabled = false;
    responseDiv.innerHTML = response;
}
