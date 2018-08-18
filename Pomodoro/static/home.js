// alert("Hello C4T4, I'm a JS script");

console.log("Hello, this is c4t4 loggin");

var title = "Byebye";
console.log(title);

m = 23;
console.log(m);

// function foo() {
//     setTimeout(foo, 3000);
//     console.log("Bar");
// }

// console.log("Start")
// // foo();

// foo()
 
var minutes = 25;
var seconds = 0; 

function runner() {
    if (seconds == 0) {
        if (minutes == 0) {
            console.log ("Out of time");

        }else {
            minutes -=1;
            seconds = 59;
            setTimeout(runner, 100);
            if (minutes < 10) minutes = "0" + minutes;
            btnStart.disabled = false; 
        }
    }else {
        seconds -=1;
        setTimeout(runner, 100);
        if (seconds < 10) seconds = "0" + seconds;
    }

    
    

    var timerMinute = document.getElementById("timer_minute")
    timerMinute.innerHTML = minutes
    var timerSecond = document.getElementById("timer_second")
    timerSecond.innerHTML = seconds
    console.log(minutes)
    console.log(seconds)
}

function onStartClick() {
    var titleContent = document.getElementById("title_content");
    titleContent.innerHTML = "Timer Running";    
    runner();   
    var btnStart = document.getElementById("btn_start");
    btnStart.disabled = true 
}

function onStopClick() {
    alert ("Stop Clicked");
}



