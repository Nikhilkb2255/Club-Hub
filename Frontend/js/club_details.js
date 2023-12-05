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
            const joinCell = row.insertCell(2)

            var button = document.createElement("button");
            button.innerHTML = "Join";

            button.onclick = function() {
              data = {
                'username':localStorage.getItem('username'),
                'clubname':clubName
              }

              fetch('http://localhost:8000/clubhub/join/', {
              method: 'POST',
              headers: {
                  'Content-Type': 'application/json',
              },
              body: JSON.stringify(data),
              })
              .then(response => response.json())
              .then(data => {
                alert("You Have Joined " + clubName + ' Club !')
                button.disabled;
              })

            };
  
            nameCell.innerHTML = clubName;
            advisorCell.innerHTML = clubDetails.ClubAdvisor;
            joinCell.appendChild(button);
          }
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });