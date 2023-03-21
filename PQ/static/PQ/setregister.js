
document.addEventListener("DOMContentLoaded", function () {
    var RegisterModal = new bootstrap.Modal(document.getElementById('registermodal'), {  keyboard: false,
        backdrop: 'false'})

    var LoginModal = new bootstrap.Modal(document.getElementById('loginmodal'), {  keyboard: false,
        backdrop: 'false'})
        
    LoginModal.toggle()
    
    document.querySelector("#loginbutton").addEventListener("click", e => {
    //1
    RegisterModal.toggle()
    //2
    LoginModal.toggle()
    });

    document.querySelector("#registerbutton").addEventListener("click", e => {
    //1
    LoginModal.toggle()
    //2
    RegisterModal.toggle()
    });

//I can add here frontend validation for the login and register via API, before sending to the server. 
})

