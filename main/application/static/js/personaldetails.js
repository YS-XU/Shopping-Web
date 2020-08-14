//get password input fields
var current_password = document.getElementById('currentpass');
var new_password = document.getElementById('newpassword');
var update_pass_btn = document.getElementById('password-update-btn');
var empty_field_message = document.getElementById('empty-field-msg'); //span for message validating empty field, or same current pass and new pass
update_pass_btn.disabled = true; //disable the button first

//Make sure password field is not empty
function validateFields(){
  console.log('running function')
  console.log(current_password.value.length)

  if(current_password.value.length > 0  && new_password.value.length > 0){
      if(current_password.value === new_password.value){ //validate if current pass and new pass is equal
        update_pass_btn.disabled = true;
        empty_field_message.innerHTML = 'Please choose a password that is different from your current password!' //prompt user to choose a different password
        console.log('same password as before!');
      }else{
        console.log('different passwords ! good to go!');
        update_pass_btn.disabled = '';
        empty_field_message.innerHTML = '';
      }
  }else{
    update_pass_btn.disabled = true; //disable the button
    empty_field_message.innerHTML = "Don't leave fields empty!"; //send message into the span
  }
}
