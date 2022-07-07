console.log("hello")
fetch('1-1000.txt')
    .then(response => response.text())
    .then(data => console.log(data));