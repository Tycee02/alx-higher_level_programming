#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Usage: node get_movie_characters.js <movie_id>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch movie details. Status code:', response.statusCode);
  } else {
    try {
      const movie = JSON.parse(body);
      const characters = movie.characters;
      printCharacters(characters, 0);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});

function printCharacters (characters, index) {
  if (index >= characters.length) {
    return;
  }

  const characterUrl = characters[index];
  request.get(characterUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else if (response.statusCode !== 200) {
      console.error('Failed to fetch character details. Status code:', response.statusCode);
    } else {
      try {
        const character = JSON.parse(body);
        console.log(character.name);
        printCharacters(characters, index + 1);
      } catch (parseError) {
        console.error('Error parsing character details:', parseError);
      }
    }
  });
}
