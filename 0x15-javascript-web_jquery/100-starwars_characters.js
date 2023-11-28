#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, function (erro, respo, body) {
  if (!erro) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (erro, respo, body) {
        if (!erro) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
