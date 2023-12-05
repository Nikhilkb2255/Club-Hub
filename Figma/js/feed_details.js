document.addEventListener("DOMContentLoaded", function () {
    const feedbackTable = document.getElementById("feedbackTable").getElementsByTagName('tbody')[0];
  
    fetch('http://localhost:8000/clubhub/feedback/')
      .then(response => response.json())
      .then(data => {
        console.log(data)
        for (const Feedback in data) {
          if (data.hasOwnProperty(Feedback)) {
            const feedbackDetails = data[Feedback];
            const row = feedbackTable.insertRow();
  
            const eventCell = row.insertCell(0);
            const feedCell = row.insertCell(1);
            const userCell = row.insertCell(2);
  
            eventCell.innerHTML = feedbackDetails.eventName;
            feedCell.innerHTML =feedbackDetails.Feedback;
            userCell.innerHTML = feedbackDetails.User;
          }
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });