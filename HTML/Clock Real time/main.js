const hourE1 = document.querySelector(".hour");
const minE1 = document.querySelector(".min");
const secE1 = document.querySelector(".sec");

setInterval(() => {
    const date = new Date();
    const hourDeg = (date.getHours() /12) * 360 - 90;
    const minDeg = (date.getMinutes() /60) * 360 - 90;
    const secDeg = (date.getSeconds() /60) * 360 - 90;

    hourE1.style.transform = `rotate(${hourDeg}deg)`;
    minE1.style.transform = `rotate(${minDeg}deg)`;
    secE1.style.transform = `rotate(${secDeg}deg)`;
}, 1000);
