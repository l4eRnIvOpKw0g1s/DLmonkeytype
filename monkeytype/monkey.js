console.log("hello")
fetch('file:///C:/Users/david/code/monkeytype/1-1000.txt')
    .then(response => response.text())
    .then(data => console.log(data));