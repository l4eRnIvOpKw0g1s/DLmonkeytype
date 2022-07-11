//why dont you update
const textbox = document.getElementById('textbox');
const count = document.getElementById('count');
const timerDisplay = document.getElementById('timer');
var typed = [];
var currentWord = [];
var wordlist;
let end = false;
let caretPos = 0;
let caretPosLine = 0;
var rows = [];
rows.push([]);

function getRndInteger(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
};

async function fetchLibrary() {
    const result = await fetch('https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt');
    const data = await result.text();
    const wordLibrary = await data.split('\n');
    let wordlistasync = [];
    for (let i = 0; i < 25; i++) {
        wordlistasync.push(wordLibrary[getRndInteger(0, wordLibrary.length-1)].split(''));
    };

    wordlistasync.forEach((word) => {
        var singleDiv = document.createElement('div');
        word.forEach((letter) => {
            var singleLetter = document.createElement('letter');
            singleLetter.innerHTML = letter;
            singleDiv.appendChild(singleLetter);
        })
        textbox.appendChild(singleDiv);
    })
    return wordlistasync
}
async function doWork() {
    wordlist = await fetchLibrary();
    await document.addEventListener('keydown', logKey);
}

function logKey(e) {
    if (e.key === "Enter") {
        location.reload();
    }
    if (end) {
        return
    }
    var currentWordlistInd = typed.length
    var currentLetterInd = currentWord.length
    const words = Array.from(textbox.children);
    const letters = Array.from(words[currentWordlistInd+1].children);
    if (e.key === "Backspace") {
        if (currentWord.length) {
            currentWord.pop();
            caretPos -= 14.41;
            if (currentLetterInd > wordlist[currentWordlistInd].length) {
                words[currentWordlistInd+1].removeChild(words[currentWordlistInd+1].lastChild);
            } else {
                letters[currentLetterInd-1].removeAttribute('class');
            }

        } else if (typed.length > 0){
            currentWord = typed[typed.length - 1];
            caretPos -= (15 + Math.max(wordlist[currentWordlistInd-1].length-currentWord.length, 0) * 14.41);
            count.innerHTML = `${currentWordlistInd-1}` +"/25";
            typed.pop();
            rows[rows.length-1].pop(); 
        }
    }
    if (e.key === " ") {
        if (currentWord.length) {
            caretPos += 15 + Math.max(wordlist[currentWordlistInd].length-currentWord.length, 0) * 14.41;
            typed.push(currentWord);
            currentWord = [];
            count.innerHTML = `${currentWordlistInd+1}` +"/25";
            rows[rows.length-1].push(currentWordlistInd)
        }
    } else if (e.key.length === 1) {
        if (interval === null) {
            start();
        }
        
        currentWord.push(`${e.key}`);
        caretPos += 14.41;
        //writing out letters n stuff
        if (currentLetterInd >= wordlist[currentWordlistInd].length) {
            var singleLetter = document.createElement('letter');
            singleLetter.innerHTML = `${e.key}`;
            singleLetter.className = "extra"
            words[currentWordlistInd+1].appendChild(singleLetter);
        } else if (wordlist[currentWordlistInd][currentLetterInd] === currentWord[currentLetterInd]) {
            letters[currentLetterInd].className = "correct"
        } else {
            letters[currentLetterInd].className = "incorrect"
        }
    }
    caretShift(textbox.offsetWidth, currentWordlistInd);


    document.getElementById("caret").style.transform = ("translate("+`${caretPos}`+ "px, "+`${caretPosLine}` * 36.2 + "px");


    if ((typed.length === 24 && JSON.stringify(currentWord) === JSON.stringify(wordlist[24])) || (typed.length === 25)) {
        stop();
    }

}

doWork();

let seconds = 0;
let interval = null;

function timer () {
    seconds++;
    let mins = Math.floor(seconds / 60);
    let secs = seconds % 60;
    if (mins) {
        if (secs < 10) {
            timerDisplay.innerHTML = `${mins}:0${secs}`;
        } else {
            timerDisplay.innerHTML = `${mins}:${secs}`;
        }
    } else {
        timerDisplay.innerHTML = `${secs}`;
    }
}

function start () {
    interval = setInterval(timer, 1000);
}

function stop () {
    clearInterval(interval);
    interval = null;
    textbox.style.backgroundColor = (getColorFromRoot('--gray'));
    textbox.style.border = "3px solid"+ (getColorFromRoot('--yellow'));
    textbox.style.borderRadius = "15px";
    var wpm = document.createElement('div');
    wpm.innerHTML = "WPM: " + `${(((document.getElementsByClassName("correct").length)/4.25)/(seconds/60)).toFixed(2)}`
    wpm.className = "wpm"
    document.getElementById("border").appendChild(wpm);
    document.getElementById("count").remove();
    document.getElementById("caret").remove();

    end = true;
}

function getColorFromRoot(name) { 
    return(getComputedStyle(document.querySelector(':root')).getPropertyValue(name));
}

function caretShift(textboxWidth, currentWordlistInd) {
    console.log(rows)
    if (typed.length === 25) return
    let totalW = 0
    let letterW = 14.41
    let betweenW = 15
    
    if (caretPos < 0) {
        caretPosLine -= 1;
        console.log(typed)
        for (let i = 0; i < rows[0].length; i++) {
            totalW += Math.max(wordlist[rows[0][i]].length, typed[rows[0][i]].length) * letterW + betweenW;
        }
        rows.pop();
        caretPos = totalW + (Math.max(currentWord.length, wordlist[typed.length].length) * letterW + betweenW);
        return
    }

    for (let i = 0; i < rows[rows.length-1].length; i++) {
        totalW += Math.max(wordlist[rows[rows.length-1][i]].length, typed[rows[rows.length-1][i]].length) * letterW + betweenW;
    }
    if (currentWord.length > wordlist[typed.length].length) {
        if ((totalW + currentWord.length * letterW + betweenW) > textboxWidth) {
            caretPos = letterW * currentWord.length
            caretPosLine += 1
            rows.push([])
        }
    } else if ((totalW + wordlist[typed.length].length * letterW + betweenW) > textboxWidth){
        caretPos = 0;
        caretPosLine += 1;
        rows.push([])
    }    
}
