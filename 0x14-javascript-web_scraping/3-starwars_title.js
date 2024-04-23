#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const reqURL = 'https://swapi-api.alx-tools.com/api/films/';
const url = reqURL + id;
request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(body.title);
});
