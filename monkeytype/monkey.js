var fs = require('fs');
var text = fs.readFileSync("monkeytype/1-1000.txt", 'utf-8');
var textByLine = text.split('\n');
console.log (typof textByLine);
console.log (textByLine);

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
};