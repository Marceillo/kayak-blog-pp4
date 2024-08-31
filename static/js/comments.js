/* jshint esversion: 6 */
const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteButtons = document.getElementsByClassName("btn-danger");
const deleteConfirm = document.getElementById("deleteConfirm");

/*
 * Initializes edit functionality for the provided edit buttons.
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


}

/*
 * This is a delete feature for comments.
 * Before the comment delet and edit buttons,
 * where not hidden, even if you where not a author.
 * You could see the buttons I have since updated 
 * the template to hide the buttons and show only when
 * you are a author. 
 * So this code also can now check when the btn-danger is clicked.
 * Checks the comment ID and checks if user is author.
 * if not error message "You can't delete this comment.
 * If this is the user a delet form is started and the modal is shown.
 * When a confirmation button is clicked, the deleteForm is submitted.
 * The show message styles the alert error message for user feedback.
 * Then disappears after 5 seconds.  
 */

document.querySelectorAll('.btn-danger').forEach(button => {
    button.addEventListener('click', function() {
        const commentId = this.getAttribute('data-comment_id');
        const isAuthor = this.getAttribute('data-is_author');

        if (isAuthor === 'false') {
            showMessage('error', "You can't delete this comment.");
            return;
        }

        const deleteForm = document.querySelector('#deleteModal form');
        deleteForm.action = `/comment/${commentId}/delete/`;
        deleteModal.show();
    });
});


deleteConfirm.addEventListener('click', function() {
    const deleteForm = document.querySelector('#deleteModal form');
    deleteForm.submit();
});


function showMessage(type, message) {

    const messageDiv = document.createElement('div');
    messageDiv.classList.add('alert', 'alert-custom', `alert-${type}`, 'alert-dismissible', 'fade', 'show', 'text-center');
    messageDiv.innerHTML = `${message} <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>`;
    messageDiv.style.display = 'inline-block';


    const container = document.querySelector('.container');
    if (container) {
        container.insertAdjacentElement('beforebegin', messageDiv);
    }

    setTimeout(() => {
        messageDiv.remove();
    }, 5000);
}

