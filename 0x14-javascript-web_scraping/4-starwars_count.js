#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else {
    try {
      const filmsData = JSON.parse(body);
      const wedgeMovie = filmsData.results
        .filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'))
        .length;
      console.log(wedgeMovie);
    } catch {
      console.error('Error');
    }
  }
});
