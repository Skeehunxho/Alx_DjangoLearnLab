document.addEventListener("DOMContentLoaded", function loadTasks() {
    let tasks = JSON.parse(localStorage.getItem('tasks')) ||  [];
    tasks.forEach(task => addTaskToDOM(task));
    // My code
    const form = document.getElementById("To-Do List Appplication");
    const addButton = document.getElementById("add-task-btn");
    const taskInput = document.getElementById("task-input");
    const taskList = document.getElementById("task-list");
  
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      addTask();
    });
  
    // AddTask creation function
    function addTask() {
      const taskText = taskInput.value.trim();
      if (taskText === "") {
        alert("Please enter a task.");
        return;
      }
      const li = document.createElement("li");
      li.textContent = taskText;
      const removeButton = document.createElement("button");
      removeButton.textContent = "Remove";
      removeButton.className = "remove-btn";
      removeButton.onclick = function () {
        taskList.removeChild(li);
      };
      li.appendChild(removeButton);
      taskList.appendChild(li); // Correct way to add the task to the list
      taskInput.value = "";
    }
  
    // this will disable reload on click
    addButton.addEventListener("click", function (e) {
      e.preventDefault();
      addTask();
    });
  
    taskInput.addEventListener("keypress", function (event) {
      if (event.key === "Enter") {
        event.preventDefault();
        addTask();
      }
    });
  
    // Task Addition functionality
    function addTask(task, save = true){
      localStorage.setItem('tasks', JSON.stringify(storedTasks));
      addTaskToDOM(task);
  
      if (save) {
        const storedTasks = (localStorage.getItem ('tasks' || '[]'));
        storedTasks.push(taskText);
      }
    }
  
  });