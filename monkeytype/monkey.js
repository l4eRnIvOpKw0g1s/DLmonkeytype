let wordlibrary;
fetch('monkeytype/1-1000.txt')
    .then(response => response.text())
    .then(data => wordlibrary = data);

document.getElementById("words").innerHTML = wordlibrary;

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}