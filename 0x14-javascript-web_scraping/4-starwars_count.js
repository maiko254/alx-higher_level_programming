#!/usr/bin/node
const request = require('request');
const reqURL = process.argv[2];
request(reqURL, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  let count = 0;
  for (const movie of body.results) {
    const characters = movie.characters;
    if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
