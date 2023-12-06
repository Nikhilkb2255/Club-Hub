document.addEventListener("DOMContentLoaded", async function () {
  try {
    data = {
      "staffclub":localStorage.getItem("staffclub")
    }
    fetch('http://localhost:8000/clubhub/userclub/', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
      })
      .then(response => response.json())
      .then(data => {
        const tableBody = document.getElementById('registrationTable');

        data.data.forEach(user => {
          if(user.username != localStorage.getItem("username")){
          const row = tableBody.insertRow();
          const usernameCell = row.insertCell(0);
          const emailCell = row.insertCell(1);
          const departmentCell = row.insertCell(2);
          const clubCell = row.insertCell(3);
          const joinCell = row.insertCell(4)
    
                var button = document.createElement("button");
                button.innerHTML = "Delete";
    
                button.onclick = function() {
                  var data = {
                      "username":user.username,
                      "clubname": user.club
                    } 
    
                  fetch('http://localhost:8000/clubhub/userclub/', {
                  method: 'DELETE',
                  headers: {
                      'Content-Type': 'application/json',
                  },
                  body: JSON.stringify(data),
                  })
                  .then(response => response.json())
                  .then(data => {
                    alert("User Deleted")
                    window.location.reload()
                  })
    
                };
    
          usernameCell.innerHTML = user.username;
          emailCell.innerHTML = user.email;
          departmentCell.innerHTML = user.department;
          clubCell.innerHTML = user.club;
          joinCell.appendChild(button);
              }
        });
      })
  } catch (error) {
    console.error('Error:', error);
  }
});
