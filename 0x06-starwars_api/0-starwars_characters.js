#!/usr/bin/node
// prints the characters from a starwars movie passed from cmd line
let request = require('request');
const promisify = require('util').promisify;

request = promisify(request);
const num = process.argv[2];

const getChars = async () => {
  try {
    const res = await request(`https://swapi-api.alx-tools.com/api/films/${num}`);
    const chars = JSON.parse(res.body).characters;
    return chars;
  } catch (err) {
    console.log(err);
  }
};

getChars().then(async (characters) => {
  try {
    for (const character of characters) {
      const res = await request(character);
      const name = JSON.parse(res.body).name;
      console.log(name);
    }
  } catch (err) {
    console.log(err);
  }
});
