// var connection 
// document.onreadystatechange = () => {
//     if (document.readyState === 'complete') {
//         var conn = document.getElementById('connected')
//         var disconn = document.getElementById('disconnected')
//     }
//   };

var disconn
var conn
var tecla

window.onload=function(){
    disconn = document.getElementById('disconnected')
    conn = document.getElementById('connected')
    tecla =  document.getElementById('tec')
}   

connection = new WebSocket('ws://127.0.0.1:8083');


connection.onopen = function () {
    disconn.style.display = 'none';
    // disconn.innerHTML = "teste"
    conn.style.display = ""

    var pressed = document.getElementById('pressed');
};

connection.onerror = function (error) {
console.log('WebSocket Error ' + error);
};

connection.onclose = function (a){
    disconn.style.display = ''
    disconn.innerHTML += a 
    conn.style.display = 'none'
    // setTimeout(connect, 1000)
};

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
        tecla.innerText =  str
    }
};
document.onkeyup = function(evt) {
    var str = keyPressed(evt);
    pressionada[evt.keyCode - 96] = false;
    connection.send((evt.keyCode - 96)+'u');
};




// function connect(){

