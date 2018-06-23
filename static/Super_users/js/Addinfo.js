  $(function () {
        $('form').submit(upload);
    });

    function upload(event) {
        event.preventDefault();
        id = '#' + $(this).attr('id');
        //alert(id);
        data = new FormData($(id).get(0));
        //alert(data);
        // x = $("#selected_city").find(":selected").text() + $("#txt_Address").val();
        // $("#txt_Address").val(x)
        // $("#txt_specialty").val($("#selected_specialty").find(":selected").text());
        //var data = new FormData($('#frm_Login').get(0));
        //alert(data.append('id' , id));
        //alert(data['id']);
        $.ajax({
            url: '',
            type: $(this).attr('method'),

            data: data,
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
                alert('ثبت اطلاعات با موفقیت انجام شد');
            }
        });
        return false;
    };