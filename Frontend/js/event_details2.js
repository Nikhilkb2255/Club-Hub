// Add event listener to the button
document.getElementById('addButton').addEventListener('click', function() {
    // Navigate to the specified URL when the button is clicked
    window.location.href = 'file:///C:/Users/Hp/Desktop/Figma/add_event.html';
  });

  
document.addEventListener("DOMContentLoaded", function () {
    const eventTable = document.getElementById("eventTable").getElementsByTagName('tbody')[0];
  
    fetch('http://localhost:8000/clubhub/event/')
      .then(response => response.json())
      .then(data => {
        for (const eventName in data) {
          if (data.hasOwnProperty(eventName)) {
            const eventDetails = data[eventName];
            const row = eventTable.insertRow();
            const nameCell = row.insertCell(0);
            const clubCell = row.insertCell(1);
            const dateCell = row.insertCell(2);
            const timeCell = row.insertCell(3);

            const updateCell = row.insertCell(4);
            const deleteCell = row.insertCell(5);
            

            var button1 = document.createElement("button");
            button1.innerHTML = "update";
            button1.onclick = function() {
                localStorage.setItem("eventName",eventName);
                window.location.assign('update_event.html')
                };
            
            var button2 = document.createElement("button");
            button2.innerHTML = "delete";
            button2.onclick = function() {

                data = {
                    "eventname":eventName
                }

                fetch('http://localhost:8000/clubhub/event/', {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                })
        
                .then(response => response.json())
                .then(data => {
                    alert("Event Removed");
                    window.location.reload();
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
    
                };
            

            nameCell.innerHTML = eventName;
            clubCell.innerHTML = eventDetails.EventClub;
            dateCell.innerHTML = eventDetails.EvenDate;
            timeCell.innerHTML = eventDetails.EventTime;
            updateCell.appendChild(button1);
            deleteCell.appendChild(button2);
          }
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });