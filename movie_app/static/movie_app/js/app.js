let formElement = document.querySelectorAll('.form-element');

for(let i = 0; i<formElement.length; i++) {

    formElement[i].addEventListener('click', () => {
        formElement[i].style.animation = 'bckgrndChange 0.2s ease-in forwards'; 
        formElement[i].style.color = 'black';
        formElement[i].style.cursor = 'default';
        formElement[i].style.transform = 'none';
        // formElement[i].style.border = '1px solid grey'; 
    });    
}

