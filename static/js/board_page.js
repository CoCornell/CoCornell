$(document).ready(function(){

    /**
     * Delete the list if user clicks the delete button.
     */
    $("div.head span.delete")
        .click(function() {
            var list_id = $(this).attr('id').replace('list', '');
            var r = confirm("Are you sure want to delete this list?");
            if (r) {
                $.ajax({
                    url: "/api/list/" + list_id + '/',
                    type: "delete",
                    success: function(data) {
                        alert('success');
                        alert(data);
                    },
                    fail: function(data) {
                        alert('fail');
                        alert(data)
                    }
                });
                // delete the DOM
            }
        })
});

