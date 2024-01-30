#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  }
  const filmsData = JSON.parse(body);
  let wedgeMovies = 0;
  for (const film of filmsData.results) {
    if (film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      wedgeMovies++;
    }
  }
  console.log(wedgeMovies);
});
