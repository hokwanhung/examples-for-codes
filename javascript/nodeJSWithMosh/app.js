
function sayHello(name) {
    console.log('Hello ' + name); // global object in Node (window)
}

sayHello('Mosh');

// Same as global objects (window)
setTimeout();
clearTimeout();

setInterval();
clearInterval();

var message = '';
console.log(global.message); // undefined (only scoped in this JS file)

// Check what the module is and what it offers.
console.log(module);

// Load a module.
var logger = require('./logger');

console.log(logger);