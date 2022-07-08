function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
};

async function fetchLibrary() {
    const result = await fetch('https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt')
    const data = await result.text()
    const wordLibrary = await data.split('\n');
    var typelist = [];
    for (let i = 0; i < 25; i++) {
        typelist.push(wordLibrary[getRndInteger(0, wordLibrary.length-1)])
    };
    document.getElementById("words").innerHTML = typelist.join(" ");
}
fetchLibrary();

const log = document.getElementById('log');

document.addEventListener('keydown', logKey);

function logKey(e) {
    if (e.key.length === 1) {
        log.textContent += `${e.key}`;
        console.log(e.key);
    } else {
        if (e.key === "Backspace" || e.key === "Delete") {
            log.textContent = log.textContent.slice(0, -1);
        }
        if (log.textContent.slice(-1) != " " && (e.key == " " || e.key == "Enter")) {
            console.log("hello");
            log.textContent += " "; 
    }
    }
}