var wordlibrary;
fetch('monkeytype/1-1000.txt')
    .then(response => response.text())
    .then(data => wordlibrary = data.split('\n'));

console.log(typeof wordlibrary);
console.log(wordlibrary.slice(0, 50));
document.getElementById("words").innerHTML = wordlibrary;


function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
};