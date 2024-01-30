#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }
  try {
    const movieData = JSON.parse(body);
    const charactersURLs = movieData.characters;
    const fetchAndPrintCharacter = (characterURL) => {
      request.get(characterURL, (charError, charResponse, charBody) => {
        if (charError) {
          console.error(`Error fetching character: ${charError}`);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    };
    charactersURLs.reduce((promise, characterURL) => {
      return promise.then(() => new Promise(resolve => {
        fetchAndPrintCharacter(characterURL);
        setTimeout(resolve, 100);
      }));
    }, Promise.resolve());

  } catch (parseError) {
    console.error('Error');
    process.exit(1);
  }
});
