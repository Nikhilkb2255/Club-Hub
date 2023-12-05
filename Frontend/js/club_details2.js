document.addEventListener("DOMContentLoaded", function () {
    const clubTable = document.getElementById("clubTable").getElementsByTagName('tbody')[0];
  
    fetch('http://localhost:8000/clubhub/club/')
      .then(response => response.json())
      .then(data => {
        for (const clubName in data) {
          if (data.hasOwnProperty(clubName)) {
            const clubDetails = data[clubName];
            const row = clubTable.insertRow();
            
            const nameCell = row.insertCell(0);
            const advisorCell = row.insertCell(1);
  
            nameCell.innerHTML = clubName;
            advisorCell.innerHTML = clubDetails.ClubAdvisor;
          }
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });