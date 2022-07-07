console.log("hello")
fetch('monkeytype/1-1000.txt')
    .then(response => response.text())
    .then(data => document.getElementById("words").innerHTML = data);
document.getElementById("words").innerHTML = "hello";