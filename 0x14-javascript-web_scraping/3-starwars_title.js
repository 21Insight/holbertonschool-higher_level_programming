#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request.get(url, (error, response, body) => {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
