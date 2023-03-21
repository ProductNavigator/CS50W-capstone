
document.addEventListener("DOMContentLoaded", function () {
    var AddModal = new bootstrap.Modal(document.getElementById('askmodal'), {  keyboard: false,
        backdrop: 'false'})
        
    AddModal.toggle()
    
    document.querySelector("#closebutton").addEventListener("click", e => {
    //1
    AddModal.toggle()
    });



})

