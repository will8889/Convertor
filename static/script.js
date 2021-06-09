/* Define a variable for "menu-toggle input" class which the 3 bars of the recycler view implements. */
const menuToggle = document.querySelector('.menu-toggle input');
/* Define a variable for "nav ul" class which the navigation bar implements. */
const nav = document.querySelector('nav ul');

/* Function to toggle the slide animation which is used to display the recycler view. */
menuToggle.addEventListener('click', function() {
    nav.classList.toggle('slide');
})