document.addEventListener("DOMContentLoaded", function() {
    let actionForm = document.querySelector("form[action]");
    let actionSelect = document.querySelector("select[name='action']");
    
    if (actionForm && actionSelect) {
        actionForm.addEventListener("submit", function(event) {
            if (actionSelect.value === "delete_selected") {
                event.preventDefault(); // Stop the default Django behavior

                // Show confirmation popup
                let confirmDelete = confirm("Are you sure you want to delete the selected products?");
                if (confirmDelete) {
                    actionForm.submit(); // Proceed with deletion if confirmed
                }
            }
        });
    }
});