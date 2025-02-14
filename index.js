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

// searching perfectness

let numberInput = document.getElementById("jacob")
let divOutput = document.getElementById("output")

numberInput.addEventListener("input", () => {
    let num = parseFloat(numberInput.value); // Convert to a floating-point number

    if (isNaN(num)) {
      divOutput.textContent = "Please enter a valid number.";
    } else if (num < 0) {
      divOutput.textContent = "Please enter a positive number.";
    }
     else {
        divOutput.textContent = "You entered: " + num;
        // Perform calculations or other operations with the number
    }
});




