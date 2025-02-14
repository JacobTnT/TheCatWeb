function myFunction (){
    let input, filter, ul, a, i, txtValue;
    input = document.getElementById("myInput")
    filter = input.value.toUpperCase();
    ul = document.getElementById("anyUL")
    li = ul.getElementsByTagName("li")

    for (let j = 0; j < li.length; j++){
        a = li[j].getElementsByTagName("a")[0];
        txtValue = a.textContent || a.innerText
        if(txtValue.toUpperCase().indexOf(filter) > 0){
            li[j].style.display = "";
        }
        else {
            li[j].style.display = "none";
        }

    }
}