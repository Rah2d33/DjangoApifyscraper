 
document.querySelector('form').addEventListener('submit', function(event) {
    const usernameInput = document.querySelector('#username').value;
    if (!usernameInput) {
        event.preventDefault();
        alert('Please enter a username.');
    }
});
