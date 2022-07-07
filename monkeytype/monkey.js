let wordlibrary;
fetch('monkeytype/1-1000.txt')
    .then(response => response.text())
    .then(data => wordlibrary = data);

document.getElementById("words").innerHTML = wordlibrary;