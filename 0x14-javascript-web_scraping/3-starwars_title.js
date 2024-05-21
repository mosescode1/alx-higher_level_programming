#!/usr/bin/node

const res = require("request")
const fs = require("fs")
const movie_id = process.argv[2];
const url = "https://swapi-api.hbtn.io/api/films/" + movie_id;
res.get(url, (err, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const jsonBody = JSON.parse(body.body);
  console.log(jsonBody.title);
});