function check(){
    Uname=document.getElementById("Cname");
    if (Uname==""){
        alert("Please Enter your name");
        Uname.focus();
        return false
    }
}