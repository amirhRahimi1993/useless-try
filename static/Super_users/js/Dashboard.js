var previous_scroll = 0;
var timeoutId = 0;

$(document).ready(function () {

    $("form").submit(function () {
        event.preventDefault();
        id = '#' + $(this).attr('id');
        //alert(id);
        data = new FormData($(id).get(0));
        //alert(data);
        //alert($(data).serialize());
        $.ajax({
            url: '',
            data: data,
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            type: "POST",
            success: function (data) {
                alert("Success");
                alert(data.is_taken);
            },
        });
    });
});