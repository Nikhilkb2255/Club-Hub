document.addEventListener("DOMContentLoaded", function () {
    const feedbackTable = document.getElementById("feedbackTable").getElementsByTagName('tbody')[0];
  
    fetch('http://localhost:8000/clubhub/feedback/')
      .then(response => response.json())
      .then(data => {
        for (const Feedback in data) {
          if (data.hasOwnProperty(Feedback)) {
            const feedbackDetails = data[Feedback];
            var now = new Date();
            var parts = feedbackDetails.eventDate.split('-');
            var date = new Date(parts[0], parts[1] - 1, parts[2]);
            var status = "Completed"
            if(date >= now)
              status = "Upcoming"
            const row = feedbackTable.insertRow();
            const userCell = row.insertCell(0);
            const eventCell = row.insertCell(1);
            const dateCell = row.insertCell(2);
            const TimeCell = row.insertCell(3);
            const feedCell = row.insertCell(4);
            const statusCell = row.insertCell(5);
            eventCell.innerHTML = feedbackDetails.eventName;
            feedCell.innerHTML =feedbackDetails.Feedback;
            userCell.innerHTML = feedbackDetails.User;
            dateCell.innerHTML = feedbackDetails.eventDate;
            TimeCell.innerHTML = feedbackDetails.eventTime;
            statusCell.innerHTML = status;
          }
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });