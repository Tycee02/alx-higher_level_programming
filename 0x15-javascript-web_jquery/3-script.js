// adds the class red to the header element when user clicks on tag DIV#red_header using jQuery

$('DIV#red_header').click(function () {
  $('HEADER').addClass('red');
});
