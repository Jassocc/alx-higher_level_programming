#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (error, response) => {
  if (error) {
    console.error(`code: ${error.code}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
