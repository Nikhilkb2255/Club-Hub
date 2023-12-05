document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('id-Update').addEventListener('click', function(e) {
        e.preventDefault();

        var eventName = document.getElementById("eventUpdatedName").value;
        var date = document.getElementById("eventUpdateDate").value;
        var time = document.getElementById("eventUpdateTime").value;

        const data = {
            "eventName" : localStorage.getItem("eventName"),
            "eventUpdatedName": eventName,
            "eventUpdateDate" : date,
            "eventUpdateTime" : time
            };

        fetch('http://localhost:8000/clubhub/event/', {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })

        .then(response => response.json())
        .then(data => {
            alert("Event Updated !");
            console.log('Success:', data);
            window.location.assign('event_details2.html')
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});