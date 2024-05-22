#!/usr/bin/node

const resq = require('request');
const urlId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + urlId;

resq.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  // gets the characters from the movie
  const characters = JSON.parse(body).characters;
  const arr = [];
  // loop through the characters and get the names
  characters.forEach(character => {
    resq.get(character, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  });
});
