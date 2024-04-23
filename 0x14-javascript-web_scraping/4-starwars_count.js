#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node count_movies_with_character.js <api_url>');
  process.exit(1);
}

const characterId = '18'; // Wedge Antilles character ID

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch movie list. Status code:', response.statusCode);
  } else {
    try {
      const films = JSON.parse(body).results;
      const moviesWithWedgeAntilles = films.filter((film) => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
      console.log('Number of movies with Wedge Antilles:', moviesWithWedgeAntilles.length);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
