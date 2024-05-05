// script that fetches from https://hellosalut.stefanbohacek.dev/?lang=frand displays the value fetch

$('document').ready(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
