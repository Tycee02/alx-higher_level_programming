// Script that fetches the character name
// from the URL: https://swapi-api.alx-tools.com/api/films/?format=json

$.get('https://swapi.co/api/people/5/?format=json', function (data) {
  $('DIV#character').text(data.name);
});
