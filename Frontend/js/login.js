document.getElementById('hoverrr').addEventListener('click', function(e) {
    e.preventDefault();
    var username = document.getElementById("username").value
    var password = document.getElementById("password").value

    const data = {
    "username": username,
    "password": password
    };
    
    fetch('http://localhost:8000/clubhub/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })

    .then(response => response.json())
    .then(data => {
        localStorage.setItem("userid",data["userid"]);
        localStorage.setItem("username",data["username"]);
        if(data["status"] == "success"){
            if(data['staff'] == "false"){
                localStorage.setItem('userClubs', data['userClubs'])
                window.location.assign('user_home.html')
            }
            else{
                localStorage.setItem('staffClub', data["staffClub"])
                window.location.assign('club_home.html')}
        }
        else{
            alert('Incorrect Username / Password')
        }
        
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
  