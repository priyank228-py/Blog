// Add your JS here
// script.js
document.addEventListener('DOMContentLoaded', () => {
    console.log("JS Loaded");

    const flashMessages = document.querySelectorAll('.flash');
    setTimeout(() => {
        flashMessages.forEach(el => el.style.display = 'none');
    }, 4000); // hide flash messages after 4 sec
});
