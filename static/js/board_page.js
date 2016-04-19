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
     * Click on image card.
     */
    $("img.image").click(function() {
        var card_id = $(this).attr('id').replace('image', '');
        $.ajax({
            url: "/card/" + card_id + "/ocr-text/",
            type: "GET",
            dataType: "json",
            success: function(data) {
                alert(data.ocr.text);
            },
            fail: function () {}
        });
    });
});
