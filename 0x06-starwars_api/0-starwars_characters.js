#!/usr/bin/node
// prints the characters from a starwars movie passed from cmd line
let request = require('request');
const promisify = require('util').promisify;


request = promisify(request);
const num = process.argv[2];

const getChars = async () => {
  try {
    const res = await (await request(`https://swapi-api.alx-tools.com/api/films/${num}`));
    const chars = JSON.parse(res.body).characters;
    chars.forEach(getname);
  } catch (err) {
    console.log(err);
  }
};

const getname = async (character) => {
  try {
    const res = await (await request(character));
    console.log(JSON.parse(res.body).name);
  } catch (err) {
    console.log(err);
  }
};

getChars();
