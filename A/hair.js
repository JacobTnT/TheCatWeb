console.log("Hello World!")

function anyFunction(){
    let input, filter, ul,a,i,txtValue;
    input = document.getElementById("MyWaffles")
    filter = input.value.ToUpperCase();
    ul = document.getElementById('myUL')
    li = document.getElementsByTagName('li')

    for ( let j = 0; i < li.length; i++){
        a = li[i].getElementsByTagName('a')[0];
        txtValue = a.textContent || a.innerText
        if(txtValue.toUpperCase().indexOf(filter) > 0){
            li[i].style.display = ""
        }
        else{
            li[i].style.display = "none"
        }
    }
}