$(function () {
    $('form').submit(upload);
});

function upload(event) {
    data = new FormData($('form').get(0));
    //alert(data);
    // x = $("#selected_city").find(":selected").text() + $("#txt_Address").val();
    // $("#txt_Address").val(x)
    // $("#txt_specialty").val($("#selected_specialty").find(":selected").text());
    //var data = new FormData($('#frm_Login').get(0));
    //alert(data);
    $.ajax({
        url: '',
        type: $(this).attr('method'),

        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            if (data.is_correct == 'False') {
                alert("نام کاربری یا کلمه عبور شما اشتباه است");
            }
            else {
                window.location.replace(data.is_taken)
            }
        }
    });
    return false;
};
