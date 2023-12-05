document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('hoverrr').addEventListener('click', function(e) {
        e.preventDefault();
        var username = document.getElementById("uname").value
        var email = document.getElementById("email").value
        var gender = document.getElementById("genderDropdown").value
        var age = document.getElementById("age").value
        var department = document.getElementById("department").value
        var password = document.getElementById("pass").value

        const data = {
        "username" : username,
        "email" : email,
        "gender" : gender,
        "age":age,
        "department":department,
        "password" : password
        };

        fetch('http://localhost:8000/clubhub/signup/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })

        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            alert('Account registered successfully!');
            window.location.assign('login.html')
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('An error occurred while registering..');
        });
    });
});