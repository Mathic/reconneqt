// Modal edit habit form
$('#action-edit-submit').click(function(ev) {
  ev.preventDefault();
  var form = $(this).closest("form");

  $.ajax({
    type: $(this).attr('method'),
    url: $(this).attr('url'),
    data: form.serialize(),
    context: this,
    success: function(data, status) {
      $('#edit-modal').modal('toggle');
      window.location.reload(true);
    }
  });
});

$(function () {
  $('.datetime-input').datetimepicker({
    format: 'Y-m-d H:i:s',
    step: 5
  });
});
