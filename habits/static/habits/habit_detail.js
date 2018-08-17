// Sidebar menu toggle (not being used atm)
$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

// Nav bar set active button
$(document).ready(function() {
  $('li.active').removeClass('active');
  $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
});

// Bootstrap tooltip toggle
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

// Modal new habit button
$('#new-habit-button').click(function(ev){
  ev.preventDefault();
  var url = $(this).data("form");
  $('#edit-modal').load(url, function(){
    $(this).modal('show');
  });
  return false;
});

// Modal edit habit button
$('#edit-habit-button').click(function(ev){
  ev.preventDefault();
  var url = $(this).data("form");
  $('#edit-modal').load(url, function(){
    $(this).modal('show');
  });
  return false;
});

// Modal new action button
$('#new-action-button').click(function(ev){
  ev.preventDefault();
  var url = $(this).data("form");
  $('#edit-modal').load(url, function(){
    $(this).modal('show');
  });
  return false;
});

// Modal edit action button
$('.edit-action-button').click(function(ev){
  ev.preventDefault();
  var url = $(this).data("form");
  $('#edit-modal').load(url, function(){
    $(this).modal('show');
  });
  return false;
});

// var form_options = {
//   target: '#modal',
//   success: function() {  }
// }
// $('#habit-edit-form').ajaxForm(form_options);
