function refresh(){
    login_form();
}

function login_form(){
    document.getElementById("signup-form").style.display = 'none';
    document.getElementById("login-form").style.display = 'flex';
    document.getElementById("login-form-btn").style.backgroundColor = 'black';
    document.getElementById("signup-form-btn").style.backgroundColor = '';
}

function signup_form(){
    document.getElementById("login-form").style.display = 'none';
    document.getElementById("signup-form").style.display = 'flex';
    document.getElementById("signup-form-btn").style.backgroundColor = 'black';
    document.getElementById("login-form-btn").style.backgroundColor = '';
}