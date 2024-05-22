#!/usr/bin/node

const request = require('request');

const urlId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + urlId;

request.get(url, (err, response, body) => {
  if (err) {
    console.error(err);
    return;
  }
  // gets the characters from the movie
  const characters = JSON.parse(body).characters;
  const characterNames = [];

  // Function to make a request for each character
  function getCharacterName(characterUrl, index) {
    request.get(characterUrl, (err, response, body) => {
      if (err) {
        console.error(err);
        return;
      }
      const characterName = JSON.parse(body).name;
      characterNames[index] = characterName; // Store the name at the correct index
      // Check if all character names have been retrieved
      if (characterNames.length === characters.length) {
        // Print the names in order
        characterNames.forEach(name => {
          console.log(name);
        });
      }
    });
  }

  // Loop through the characters and get the names
  characters.forEach((character, index) => {
    getCharacterName(character, index);
  });
});
