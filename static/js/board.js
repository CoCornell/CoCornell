$(document).ready(function(){

    /**
     * Add class "active" to tab "Board" on navigator bar.
     */
    $("li.board").addClass("active");

    /**
     * Open the board on clicking the board.
     */
    $("div.normal")
        .click(function() {
            var id = $(this).attr('id').replace('board', '');
            window.location.href = id;
        })
        .hover(
            function() {
                $(this).css("background-color", "#005b90");
            },
            function() {
                $(this).css("background-color", "#0067a3");
            });

    $("div.new_board")
        .hover(
            function() {
                $(this).css("background-color", "#cccccc");
            },
            function() {
                $(this).css("background-color", "#e2e4e6");
            });
});
