console.log('Hello World')
// Break and conutine
// for loop
//let j = '2'
//for (j < 5){

// if (j === 5){
 //   break;
// }
// console.log(j)
//}

// while loop way


const obj = {a: 1, b: 2, c: 3};
for (let acer in obj){
    if ( acer === 'n'){
        break;
    }
console.log(obj[acer]);
}

let index = {};
index.cat = "A animal that is very furry."
index.cat = "syntaxError"

let powerUp = true;
let jumping = false;
// 1
let sol = 3;
let GasPrice1 = 5
let GasPrice2 = 4
let GasPrice3 = 6
let hyperInflation1 = 30
let hyperInflation2 = 60
//2
let alpha1 = "BOCAJ"; 
let alpha2 = "BOCJA";
let alpha3 = "JCOAB";
let alpha4 = "JAKOB";
let alpha5 = "BBBBB";  
// 3
let TicTacToe = '[[a] [b] [a]';

function handleVoterClick() {
    console.log("buitton clicked")
    fetch("http://localhost:8080/voter/update", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: "option 1",
            votes: 1
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.log(error);
    });
}

var voterButton = document.getElementById('voter_button');
voterButton.addEventListener('click', handleVoterClick);
console.log(voterButton);
