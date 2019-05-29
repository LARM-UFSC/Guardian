
var connection = new WebSocket('ws://192.168.4.1:8083');

connection.onopen = function () {
    var pressed = document.getElementById('pressed');
};

connection.onerror = function (error) {
console.log('WebSocket Error ' + error);
};

// connection.onmessage = function (e) {
// console.log('Server: ' + e.data);
// };

function keyPressed(evt){
        evt = evt || window.event;
        var key = evt.keyCode || evt.which;
        return String.fromCharCode(key); 
    };
    var pressionada = [];
    document.onkeydown = function(evt) {
        if (!pressionada[evt.keyCode - 96]){
            var str = keyPressed(evt);
            connection.send((evt.keyCode - 96)+'d'); 
            pressionada[evt.keyCode - 96] = true;
        }
    };
    document.onkeyup = function(evt) {
        var str = keyPressed(evt);
        pressionada[evt.keyCode - 96] = false;
        connection.send((evt.keyCode - 96)+'u');
    };
