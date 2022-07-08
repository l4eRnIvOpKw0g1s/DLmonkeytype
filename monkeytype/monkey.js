function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
};

async function fetchLibrary() {
    const result = await fetch('https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt')
    const data = await result.text()
    const wordLibrary = await data.split('\n');
    for (let i = 0; i < 25; i++) {
        typelist.append(wordLibrary[getRndInteger(0, wordLibrary.length-1)])
    }
    document.getElementById("words").innerHTML = typelist;
}
let typelist
fetchLibrary();