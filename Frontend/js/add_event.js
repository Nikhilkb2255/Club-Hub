document.addEventListener("DOMContentLoaded", function() {

    async function fetchData() {
        try {
          const response = await fetch('http://localhost:8000/clubhub/club/');
          const data = await response.json();
          populateOptions(data);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      }

      function populateOptions(data) {
        const select = document.getElementById('ClubDropdown');
      
        for (const key in data) {
          if (data.hasOwnProperty(key)) {
            const option = document.createElement('option');
            option.value = key;
            option.text = key;
            select.appendChild(option);
          }
        }
      }

      fetchData();

    document.getElementById('id-Add').addEventListener('click', function(e) {
        e.preventDefault();

        var club_name = document.getElementById("ClubDropdown").value
        var event_name = document.getElementById("eventName").value
        var date = document.getElementById("eventDate").value
        var time = document.getElementById("eventTime").value

        const data = {
            "eventclub" : club_name,
            "eventname" : event_name,
            "date" : date,
            "time" : time
        };

        fetch('http://localhost:8000/clubhub/event/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok.');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            // Display pop-up message on success
            alert('Event added successfully!');
            window.location.assign('event_details2.html')
        })
        .catch((error) => {
            console.error('Error:', error);
            // Display pop-up message on error
            alert('An error occurred while adding the event.');
        });
    });
});
