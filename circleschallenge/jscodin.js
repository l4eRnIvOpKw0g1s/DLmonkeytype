const colors=["#F00","#0F0","#00F","#FF0","#0FF","#F0F"];
var colorIndex = 0;

myElements = document.querySelectorAll("circle")
for (let i = 0; i < myElements.length; i++) {
    myElements[i].addEventListener("click", changeColor);
}

function changeColor() {
    colorIndex = (1 + colorIndex) % 6;
    document.circle.style.backgroundColor = "colors[colorIndex]";

}