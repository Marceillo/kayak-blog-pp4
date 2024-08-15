const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-danger");
const deleteConfirm = document.getElementById("deleteConfirm");

/*
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Fetches the content of the corresponding comment.
 * - Populates the `commentText` input/textarea with the comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });

   /* setTimeout(() => {
        messageDiv.remove();
    }, 5000);*/
}

/*
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated comment's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific comment.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */


document.querySelectorAll('.btn-danger').forEach(button => {
    button.addEventListener('click', function() {
        const commentId = this.getAttribute('data-comment_id');
        const isAuthor = this.getAttribute('data-is_author');
        if (isAuthor==='false'){
            showMessage('error', "You can't delete this comment.");
            return;
        } 
        const deleteForm = document.querySelector(`#deleteModal form`);
        deleteForm.action = `/comment/${commentId}/delete/`;
        const modal = new bootstrap.Modal(document.getElementById('deleteModal'));
        modal.show();
    });
});

function showMessage(type, message) {
    
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('alert', 'alert-custom', `alert-${type}`, 'alert-dismissible', 'fade', 'show', 'text-center');
    messageDiv.innerHTML =`${message} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>`;
    /*messageDiv.style.display = 'inline-block';*/
    
    
    const container = document.querySelector('.container');
    if(container) {
        container.insertAdjacentElement('beforebegin', messageDiv);
    }

     setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}
    


    
