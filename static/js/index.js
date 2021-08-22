function tst(){
    $("a[id^=view-paste]").click(function() {
        var uuid = $(this).data("uuid");
        $.get('/customers/display?paste_uuid=' + uuid, function(data) {
            
        });
    });
};
