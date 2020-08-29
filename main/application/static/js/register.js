// Get the elements in the document
var error_span_msg = document.getElementById('password-error-container'); //Get the span div for error messsage
var register_btn = document.getElementById('register-btn'); //register button
var register_container = document.getElementById('register-container'); //register container
var login_container = document.getElementById('login-container') // login container
var register_view_button = document.getElementById('register-view-btn'); //register view button
var login_view_button = document.getElementById('login-view-btn') //login view button
showLogin(); //Show login first
hideSpan(); // Hide the error message span

function checkIfMatch(){
  if(document.getElementById('password1').value !== document.getElementById('password2').value){ //if both password fields dont match then ... display the error message, disable the register button
      error_span_msg.hidden = false;
      register_btn.disabled = true;
  }
  else{
    error_span_msg.hidden = true; //else enable the register button and hide the error message
    register_btn.disabled = false;
  }
}

function hideSpan(){ //Function to hide the span
  error_span_msg.hidden = true;
}

function showLogin() { //disable register and enable log in, change font sizes -- change bottom border
  register_container.hidden = true;
  login_container.hidden = false;
  login_view_button.style.borderBottom = "3px solid black";
  register_view_button.style.borderBottom = "1px solid grey"
}

function showRegister() { //disable login  and enable register -- change the bottom border
  register_container.hidden =false;
  login_container.hidden = true;
  register_view_button.style.borderBottom = "3px solid black";
  login_view_button.style.borderBottom = "1px solid grey"
}
