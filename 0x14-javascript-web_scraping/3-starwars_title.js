#!/usr/bin/node
// Print the title of the Star Wars episode passed as argument

const request = require('request');
const episode = process.argv[2];

request('https://swapi-api.hbtn.io/api/films/' + episode, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
});
