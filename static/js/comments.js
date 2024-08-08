const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementById("id_body");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
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


 /*for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("data-comment_id");
        deleteConfirm.href = `comment/${commentId}/delete/`;
        deleteModal.show();
    });
}*/

document.addEventListener("DOMContentLoaded", function () {
 

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            // Correct URL structure
            deleteConfirm.href = `/comment/${commentId}/delete/`;
            deleteModal.show();
        });
    }
});

/*  path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'), 
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if not comment.can_modify(request.user):
        return HttpResponseForbidden("You can't edit this comment")
    if request.method == 'POST':
        post_slug = comment.post.slug
        comment.delete()
        return redirect('post_detail', slug=post_slug)

    return render(request, 'blog/delete_comment.html', {'comment': comment})

*/ 


    
