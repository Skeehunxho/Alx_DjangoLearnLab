document.addEventListener('DOMContentLoaded', (event) => {
    // Your code here
  
    const form = document.getElementById('registration-form');
    const feedback = document.getElementById('form-feedback');
  
    form.addEventListener('submit', function(e) {
      e.preventDefault();
    })
  })
  
  // Retrieve user input and value trim
    const username = document.getElementById('username').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
  
    // Validation Variables
    var isValid = 'true';
   
  // Declare an array to store validation error messages
  let messages = [];
  
  // Example function to add a validation error message
  function addErrorMessage(message) {
      messages.push(message);
  }
  
  // Example validation check
  let isValid = true;
  if (username.length < 6) {
      addErrorMessage("Username must be at least 6 characters long.");
      isValid = false;
  }
  
  // Get the feedbackDiv element
  let feedbackDiv = document.getElementById("feedbackDiv");
  
  // Make feedbackDiv visible
  feedbackDiv.style.display = "block";
  
  if (isValid) {
      // If isValid is true, display success message
      feedbackDiv.textContent = "Registration successful!";
      feedbackDiv.style.color = "#28a745";
  } else {
      // If isValid is false, display error messages
      feedbackDiv.innerHTML = messages.join("<br>");
      feedbackDiv.style.color = "#dc3545";
  }
   
  // validate password
  const passwordInput = document.getElementById('password');
  const passwordError = document.getElementById('passwordError')
   let isValid = True;
  if(password.length < 8){
    addErrorMessage = ('Password must be at least 8 characters long.');
    isValid =false;
  }
  
  // validate email
  const emailInput = document.getElementById('email')
  const emailerror = document.getElementById('emailError')
  let isValid = True;
  if (!email.includes('@','.')) {
  addErrorMessage = ('Please enter a valid email address.');
  isValid = false;
  }