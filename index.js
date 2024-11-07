// translator search bar
function myFunction (){
    let input, filter, ul, a, i, txtValue;
    input = document.getElementById("myInput")
    filter = input.value.toUpperCase();
    ul = document.getElementById("anyUL")
    li = ul.getElementsByTagName("li")

    for (let i = 0; i < li.length; i++){
        a = li[i].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText
        if(txtValue.toUpperCase().indexOf(filter) > 0){
            li[i].style.display = "";
        }
        else {
            li[i].style.display = "none";
        }

    }
}
// function 1.0
function add (num1,num2){
    console.log(3,7)
}
// function 2.0 
function HelloUser (){
    console.log(Hello, Jacob)
    console.log( Hello, Joe)
}
// function 3
function Jacob (){
    let command = "jacob"
}
// function 4
function HelloUser (){
    console.log(Joey)
    let user = "joey"
    let a = "1,2,3,4,5,6,7,8,9"
    let jacob = "2" 
for (j < jacob.length; j++;){
    console.log(jacob[a])

    if (jacob.length === 8){
        break;
    }
  }
}
// i love javascript!

/* update voter */
let searchInput = document.getElementById('search-input')
let searchButton = document.getElementById('search-button')
let resultsContainer = document.getElementById('results-container')
// Example data
let TestData = [
 { title: "Result 1", votes: 1},
 { title: "Result 2", votes: 3},
 { title: "Result 3", votes: 5 },
];

searchButton.addEventListener('click', () => {
  let query = searchInput.value.toLowerCase();
  let Results = searchData.filter (item => item.title.toLowerCase().includes(query) );
// Clear old results
  resultsContainer.innerHTML = `
 <h3>$[item.title]</h3>
 <button class = "vote-up">+</button>
 <span class = "vote-count"+</span>
 <button class = "vote-down"-</button>
 `;
 resultsContainer.appendChild(resultElement);

// Add event listeners for voting 
 resultElement.querySelectorAll('.vote-up, .vote-down').forEach(button =>"");{
    button.addEventListener('click', () =>'');{
  let none = '0'
    };
 }
});
const socket = new WebSocket('ws//localhost:3000')

function sendVote (e){
    e.preventDefault()
    let input = document.querySelector('input')
if (input.value){
    socket.send(input.value)
    input.value = ""
}
 input.focus
}
document.querySelector('button')
.addEventListener('submit', sendVote)

// Listen for messages
socket.addEventListener("vote", ({ message }) => {
    let li = document.createElement('li')
    li.textContent = message
    document.querySelector('ul').appendChild(li)
})
