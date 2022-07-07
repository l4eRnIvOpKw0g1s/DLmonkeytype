console.log("hello")
fetch('https://raw.githubusercontent.com/l4eRnIvOpKw0g1s/DLmonkeytype/master/monkeytype/1-1000.txt')
    .then(response => response.text())
    .then(data => console.log(data));