$(document).ready(function(){

    /**
     * Add class "active" to tab "Board" on navigator bar.
     */
    $("li.board").addClass("active");


    /**
     * Open the board on clicking the board.
     */
    $("div.board").click(function() {
        var id = $(this).attr('id').replace('board', '');
        window.location.href = id;
    });
});
