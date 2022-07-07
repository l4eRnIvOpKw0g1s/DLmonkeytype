var wordlibrary;
fetch('monkeytype/1-1000.txt')
    .then(response => response.text())
    .then(data => wordlibrary = String(data.split('\n')));

console.log(typeof wordlibrary);
console.log(wordlibrary);
document.getElementById("words").innerHTML = wordlibrary;


function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
};