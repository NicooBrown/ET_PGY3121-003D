function updateClock() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var seconds = now.getSeconds();

    hours = addZeroPadding(hours);
    minutes = addZeroPadding(minutes);
    seconds = addZeroPadding(seconds);

    var timeString = hours + ":" + minutes + ":" + seconds;

    document.getElementById('clock').innerHTML = timeString;
}

function addZeroPadding(value) {
    if (value < 10) {
        return "0" + value;
    }
    return value;
}

setInterval(updateClock, 1000);
