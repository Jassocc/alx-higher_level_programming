#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } catch (parseError) {
      console.log('Error');
    }
  }
});
