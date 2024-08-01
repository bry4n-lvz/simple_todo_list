const modal = document.getElementById("modal");
const createButton = document.getElementById("createTaskButton");
const cancelButton = document.getElementById("cancelButton");

createButton.addEventListener("click", function() {
    modal.style.display = "flex";
});

cancelButton.addEventListener("click", function() {
    modal.style.display = "none";
});

document.addEventListener('DOMContentLoaded', (event) => {
    const checkboxes = document.querySelectorAll('.taskCheckbox');

    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            if (this.checked) {
                const taskId = this.getAttribute('data-task-id');
                
                fetch('/delete_task', {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ taskId: taskId })
                })
                .then(response => {
                    if (response.ok) {
                        window.location.reload()
                    } else {
                        alert('Failed to delete task.');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('An error occurred.');
                });
            };
        });
    });
});
