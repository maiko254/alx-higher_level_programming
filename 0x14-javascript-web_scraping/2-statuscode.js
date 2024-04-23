#!/usr/bin/node
const request = require('request');
const reqURL = process.argv[2];
request(reqURL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log('code: ', response.statusCode);
});
