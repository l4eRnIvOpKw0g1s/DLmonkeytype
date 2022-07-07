let words;
fetch('monkeytype/1-1000.txt')
    .then(response => response.text())
    .then(data => words = data);

console.log(typeof words);
let wordlibrary = words.split(" ");
console.log(wordlibrary.slice(0, 50));
document.getElementById("words").innerHTML = wordlibrary;


function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
};