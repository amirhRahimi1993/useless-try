$("#btn_Update").click(function () {
        event.preventDefault()
      var dr_name = $('#txt_name').val();
      var dr_family = $('#txt_family').val();
      var dr_address = $('#txt_address').val();
      var dr_gmap = $('#txt_gmap').val();
      var dr_mbl = $('#txt_mobile').val();
      var dr_tel = $('#txt_telephone').val();
      var dr_speciality = $('#txt_speciality').val();
      var dr_id= $('#get_field_id').text();

      $.ajax({
        url: '/ajax/Update_dr/',
        data: {
            'dr_name': dr_name,
            'dr_family' : dr_family,
            'dr_address' : dr_address,
            'dr_gmap' : dr_gmap,
            'dr_mbl' : dr_mbl,
            'dr_tel' : dr_tel,
            'dr_speciality' : dr_speciality,
            'id' : dr_id

        },
        dataType: 'json',
        success: function (data) {
            alert(data.is_taken)

        }
      });

    });