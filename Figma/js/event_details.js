document.addEventListener("DOMContentLoaded", function () {
    const eventTable = document.getElementById("eventTable").getElementsByTagName('tbody')[0];
  
    fetch('http://localhost:8000/clubhub/event/')
      .then(response => response.json())
      .then(data => {
        for (const eventName in data) {
          if (data.hasOwnProperty(eventName)) {
            const eventDetails = data[eventName];
            var userClubs = localStorage.getItem('userClubs');
            if(userClubs.includes(eventDetails.EventClub)){
            const row = eventTable.insertRow();
            const nameCell = row.insertCell(0);
            const clubCell = row.insertCell(1);
            const dateCell = row.insertCell(2);
            const timeCell = row.insertCell(3);
            const feedCell = row.insertCell(4);
  
            var button = document.createElement("button");
            button.innerHTML = "Add feedback / suggestions";
            button.onclick = function() {

              localStorage.setItem('eventName', eventName);
              window.location.assign('feedback.html')

            };

            nameCell.innerHTML = eventName;
            clubCell.innerHTML = eventDetails.EventClub;
            dateCell.innerHTML = eventDetails.EvenDate;
            timeCell.innerHTML = eventDetails.EventTime;
            feedCell.appendChild(button);
          }
        }
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });