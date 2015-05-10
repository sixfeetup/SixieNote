(function($) { $(function() {
    // allow whole list item to note to be clickable
    $("#notes li").click(function(){
        location.assign($(this).attr("data-url"));
    });
    
    // add Title placeholder
    $("#id_title").attr("placeholder", "Title your note");
    
    // set sidebar height
    $('#sidebar').css("height", window.innerHeight - 55 );


    $(document).ready(function(){
       $("#delete-note").click(function(e){
            e.preventDefault();
            if (window.confirm("Are you sure?")) {
               $("#delete-note-form").submit();
           }
       });
    });

}); })(jQuery);
