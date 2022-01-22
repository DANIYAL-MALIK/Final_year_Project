function check(){
    Uname=document.getElementById("Cname").value;
    Email=document.getElementById("Cemail").value;
    Address=document.getElementById("Caddress").value
    if (Uname==""){
        alert("Please Enter your name");
        Uname.focus();
        return false
    }
    else if(Email==""){
        alert("Please Enter your email");
        Uname.focus();
        return false;
    }
    else if(Address==""){
        alert("Please Enter your Complete Address");
        Uname.focus();
        return false;
    }
}
function logincheck(){
    Uname=document.getElementById("LoginName").value;
    Password=document.getElementById("LoginPassword").value;
    if (Uname==""){
        alert("Please Enter your name");
        Uname.focus();
        return false
    } 
    else if (Password==""){
        alert("Please enter password");
        Password.focus();
        return false
    }   
  
}