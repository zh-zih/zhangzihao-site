const aboutButton = document.getElementById('about-button');

aboutButton.addEventListener('click', function(e) {
    e.preventDefault();
    // Toggle the 'show-intro' class on the body
    if (document.body.classList.contains('show-intro')) {
        document.body.classList.remove('show-intro');
        aboutButton.innerHTML = "about";
    } else {
        document.body.classList.add('show-intro');
        aboutButton.innerHTML = "close";
    }
});