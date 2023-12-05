document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('id-Submit').addEventListener('click', function(e) {
        e.preventDefault();

        var feedback = document.getElementById("Feedback").value

        const data = {
            "username":localStorage.getItem('username'),
            "eventname":localStorage.getItem('eventName'),
            "feedback" : feedback,
            };

        fetch('http://localhost:8000/clubhub/feedback/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })

        .then(response => response.json())
        .then(data => {
            alert("Feedback Added !")
            console.log('Success:', data);
            window.location.assign('event_details.html')
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});