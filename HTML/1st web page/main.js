const wrapper = document.querySelector(".wrapper");
const wrapper2 = document.querySelector(".wrapper2");
const wrapper3 = document.querySelector(".wrapper3");
const wrapper4 = document.querySelector(".wrapper4");
const wrapper5 = document.querySelector(".wrapper5");

const loginLink = document.querySelector(".login-link");
const registerLink = document.querySelector(".reg-link");
const login2Link = document.querySelector(".login2-link");
const fpwLink = document.querySelector(".fpw-link");
const  btnPopup = document.querySelector(".btn-login");

const  iconClose1 = document.querySelector(".icon-close1");
const  iconClose2 = document.querySelector(".icon-close2");
const  iconClose3 = document.querySelector(".icon-close3");
const  iconClose4 = document.querySelector(".icon-close4");

const contactLink = document.querySelector(".Contact");
const servLink = document.querySelector(".Services");
const aboutLink = document.querySelector(".about");
const homeLink = document.querySelector(".home");

const menu = document.querySelector("#menu-icon");
const navigation = document.querySelector(".navigation");


registerLink.addEventListener('click', () => {
    wrapper.classList.add('ac1');
    wrapper5.classList.add('active-popup');
    
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('ac1');
});

loginLink.addEventListener('click', () => {
    wrapper.classList.remove('ac2');
    wrapper.classList.remove('ac3');
});

fpwLink.addEventListener('click', () => {
    wrapper.classList.add('ac2');
});

login2Link.addEventListener('click', () => {
    wrapper.classList.add('ac3');
    wrapper.classList.remove('ac4');
});

btnPopup.addEventListener('click', () => {
    
    wrapper.classList.add('active-popup');
    navigation.classList.remove('open');
    menu.classList.remove('bx-x');
    wrapper2.classList.remove('active-popup');
    wrapper.classList.remove('ac1');
    wrapper.classList.remove('ac2');
    wrapper.classList.remove('ac3');  
    wrapper3.classList.remove('active-popup');
    wrapper4.classList.remove('active-popup');
    wrapper5.classList.add('active-popup');
    btnPopup.classList.add('press')
});

iconClose1.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
    wrapper5.classList.remove('active-popup');
    btnPopup.classList.remove('press')

});

contactLink.addEventListener('click', () => {
    wrapper2.classList.add('active-popup');
    wrapper.classList.remove('active-popup');
    wrapper3.classList.remove('active-popup');
    wrapper4.classList.remove('active-popup');
    wrapper5.classList.add('active-popup');
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('open');
});

iconClose2.addEventListener('click', () => {
    wrapper2.classList.remove('active-popup');
    wrapper.classList.remove('active-popup');
    wrapper5.classList.remove('active-popup');
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('open');
});

iconClose3.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
    wrapper2.classList.remove('active-popup');
    wrapper3.classList.remove('active-popup');
    wrapper4.classList.remove('active-popup');
    wrapper5.classList.remove('active-popup');
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('open');
});

iconClose4.addEventListener('click', () => {
    wrapper.classList.remove('active-popup');
    wrapper2.classList.remove('active-popup');
    wrapper3.classList.remove('active-popup');
    wrapper4.classList.remove('active-popup');
    wrapper5.classList.remove('active-popup');
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('open');
});

aboutLink.addEventListener('click', () => {
    wrapper4.classList.add('active-popup');
    wrapper.classList.remove('active-popup');
    wrapper2.classList.remove('active-popup');
    wrapper3.classList.remove('active-popup');
    wrapper5.classList.add('active-popup');
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('open');
});

servLink.addEventListener('click', () => {
    wrapper3.classList.add('active-popup');
    wrapper.classList.remove('active-popup');
    wrapper2.classList.remove('active-popup');
    wrapper4.classList.remove('active-popup');
    wrapper5.classList.add('active-popup');
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('open');
});

homeLink.addEventListener('click', () => {
    wrapper5.classList.remove('active-popup');
    wrapper.classList.remove('active-popup');
    wrapper2.classList.remove('active-popup');   
    wrapper3.classList.remove('active-popup');   
    wrapper4.classList.remove('active-popup');
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('open');   
});

var typed = new Typed(".mt", {
    strings: ["Web Developer.", "Youtuber.", "Vloger."],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true
});


menu.addEventListener('click', () => {
    menu.classList.toggle('bx-x');
    navigation.classList.toggle('open');
});