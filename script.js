function checkServerStatus() {
    var serverInput = document.getElementById("server-input").value;

    // Make a request to the API
    fetch('https://api.example.com/check-status?server=' + serverInput)
        .then(function(response) {
            if (response.ok) {
                return response.text();
            } else {
                throw new Error('Server request failed.');
            }
        })
        .then(function(data) {
            // Process the response data
            var statusResult = document.getElementById("status-result");
            statusResult.textContent = data;
        })
        .catch(function(error) {
            console.log(error);
        });
}