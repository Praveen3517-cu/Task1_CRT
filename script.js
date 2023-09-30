document.addEventListener("DOMContentLoaded", function() {
    const addTaskForm = document.getElementById("addTaskForm");
    const taskList = document.getElementById("taskList");
    const addTaskButton = document.getElementById("addTaskButton");

    // Function to create a new task element
    function createTaskElement(taskName, priority, dueDate) {
        const listItem = document.createElement("li");
        listItem.innerHTML = `
            <span>${taskName}</span>
            <span>Priority: ${priority}</span>
            <span>Due Date: ${dueDate}</span>
            <div class="task-actions">
                <button class="complete-button">Mark as Complete</button>
                <button class="remove-button">Delete</button>
            </div>
        `;

        // Event listener for completing a task
        const completeButton = listItem.querySelector(".complete-button");
        completeButton.addEventListener("click", function() {
            listItem.classList.toggle("completed");
            completeButton.textContent = listItem.classList.contains("completed") ? "Mark as Incomplete" : "Mark as Complete";
        });

        // Event listener for deleting a task
        const removeButton = listItem.querySelector(".remove-button");
        removeButton.addEventListener("click", function() {
            taskList.removeChild(listItem);
        });

        return listItem;
    }

    // Event listener for adding a new task
    addTaskButton.addEventListener("click", function(e) {
        e.preventDefault();

        const taskName = document.getElementById("taskName").value;
        const priority = document.getElementById("priority").value;
        const dueDate = document.getElementById("dueDate").value;

        if (taskName.trim() === "") {
            alert("Please enter a task name.");
            return;
        }

        // Create a new task element and append it to the task list
        const listItem = createTaskElement(taskName, priority, dueDate);
        taskList.appendChild(listItem);

        // Clear the form fields
        document.getElementById("taskName").value = "";
        document.getElementById("priority").value = "high";
        document.getElementById("dueDate").value = "";
    });
});