#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];
const characterId = 18;
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }
  const filmsData = JSON.parse(body).results;
  const numberOfMovies = filmsData.filter((film) =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  ).length;
  console.log(numberOfMovies);
});
