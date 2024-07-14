function checkAnswer() {
    // function body
    var correctAnswer = "4";
    
    // Retrieve the User’s Answer
    var usersAnswer=document.querySelector('input[name="quiz"]:checked').value;
  
    // Compare the User’s Answer with the Correct Answer
    if (userAnswer === correctAnswer) {
      document.getElementById('feedback').textContent='"Correct! Well done."'
    }
    else { 
      document.getElementById('feedback').textContent= "That's incorrect. Try again!"
    }
  
  }
  
    // Add an Event Listener to the Submit Button
    document.getElementById('submit-answer').addEventListener('click', checkAnswer);