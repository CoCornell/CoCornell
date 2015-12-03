$(document).ready(function(){

    /**
     * Delete the list if user clicks the delete button.
     */
    $("div.head span.delete")
        .click(function() {
            var list_id = $(this).attr('id').replace('delete_list', '');
            var r = confirm("Are you sure want to delete this list?");
            if (r) {
                $.ajax({
                    url: "/list/" + list_id + '/',
                    type: "delete",
                    success: function() {
                        $("div.list#list" + list_id).remove(); // delete DOM
                    },
                    fail: function() {}
                });
            }
        });
});

