#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  } else if (response.statusCode === 200) {
    const filmsData = JSON.parse(body).results;
    let counter = 0;
    for (const a in filmsData) {
      const charas = filmsData[a].characters;
      for (const b in charas) {
        if (charas[b].includes('18')) {
          counter++;
        }
      }
    }
    console.log(counter);
  } else {
    console.log('Error code:' + response.statusCode);
  }
});
