$(document).ready(function(){

    /**
     * Delete the list if user clicks on the delete button.
     */
    $("div.head span.delete")
        .click(function() {
            var list_id = $(this).attr('id').replace('delete_list', '');
            var r = confirm("Are you sure want to delete this list?");
            if (r) {
                $.ajax({
                    url: "/list/" + list_id + "/",
                    type: "delete",
                    success: function() {
                        $("div.list#list" + list_id).remove(); // delete DOM
                    },
                    fail: function() {}
                });
            }
        });

    /**
     * Delete the card if user clicks on the delete button.
     */
    $("div.card span.delete")
        .click(function() {
            var card_id = $(this).attr('id').replace('delete_card', '');
            $.ajax({
                url: "/card/" + card_id + "/",
                type: "delete",
                success: function() {
                    $("div.card#card" + card_id).remove();
                },
                fail: function() {}
            });
        });

    //$("div.list:last-of-type").height($("div.list:first-child").height());

    /**
     * Delete image card button.
     */
    $("button.btn-delete-image").click(function() {
        var card_id = $(this).attr('id').replace('delete', '');
        $.ajax({
            url: "/card/" + card_id + "/",
            type: "DELETE",
            dataType: "json",
            success: function(data) {
                if (data.deleted) {
                    $("div.modal-backdrop").remove()
                    $("div.modal#modal" + card_id).remove();
                    $("img.image#image" + card_id).remove();
                }
            }
        });
    });

    /**
     * Click on show button.
     */
    $("button.btn-show").click(function() {
        var card_id = $(this).attr('id').replace('show', '');
        var this_button = $(this);
        if (this_button.text() != "Show Image") {
            // Show text
            $.ajax({
                url: "/card/" + card_id + "/ocr-text/",
                type: "GET",
                dataType: "json",
                success: function(data) {
                    $("div#modal" + card_id + " div.modal-body").html("<p>" + data.ocr.text + "</p>");
                    this_button.text("Show Image");
                },
                fail: function () {}
            });
        } else {
            // Show image
            var image_name = this_button.attr('data-image-name');
            $("div#modal" + card_id + " div.modal-body").html("<img class='modal-image' src='/static/uploads/" + image_name + "'>");
            this_button.text("Show OCR Text");
        }
    });

    /**
     * Add OCR text to pop-up modal.
     */
    $("img.image").click(function() {
        var card_id = $(this).attr('id').replace('image', '');
        var image_name = $(this).attr('data-image-name');
        $("div#modal" + card_id + " div.modal-body").html("<img class='modal-image' src='/static/uploads/" + image_name + "'>");
    });
});
