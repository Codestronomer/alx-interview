#!/usr/bin/node
// prints the characters from a starwars movie passed from cmd line
let request = require('request')
const promisify = require('util').promisify

// turn module to a promise object
request = promisify(request);

const num = process.argv[2];

const getChars = async () => {
	const res = await request(`https://swapi-api.alx-tools.com/api/films/${num}`);
	if (res.statusCode == "200") {
		const chars = JSON.parse(res.body).characters;
		chars.forEach(getname)
	}
}

const getname = async (character) => {
	const res = await request(character);
	console.log(JSON.parse(res.body).name);
}

getChars();
