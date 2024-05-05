// script that toggles the class of the header element when user clicks on the tag DIV#toggle_header

$('DIV#red_header').click(function () {
  $('HEADER').toggleClass('green red');
});
