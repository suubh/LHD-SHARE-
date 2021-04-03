
var numberOfDrumButtons = document.querySelectorAll(".drum").length;
for (var i = 0; i < numberOfDrumButtons; i++) {

    document.querySelectorAll(".drum")[i].addEventListener("click", function () {
        var innerText = this.innerHTML;
        makeSound(innerText);
        
    });
}

document.addEventListener("keydown",function(event){
    makeSound(event.key);
    
} );




function makeSound(key) {
    switch (key) {
        case 'w':
            var tom1 = new Audio("sounds/sounds_tom-1.mp3");
            tom1.play();
            break;
        case 'a':
            var tom2 = new Audio("sounds/sounds_tom-2.mp3");
            tom2.play();
            break;
        case 's':
            var tom3 = new Audio("sounds/sounds_tom-3.mp3");
            tom3.play();
            break;
        case 'd':
            var tom3 = new Audio("sounds/sounds_tom-3.mp3");
            tom3.play();
            break;
            
        
        default:
            console.log("key was pressed");
    }
}


