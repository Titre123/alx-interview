#!/usr/bin/node

const util = require('util');
const request = require('request');
const rs = util.promisify(request);

async function body () {
  const res = await rs(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`);
  const characters = await JSON.parse(res.body).characters;
  const tot = characters.map(item => {
    return rs(item);
  });
  Promise.all(tot).then(value => {
    value.map(ite => {
      console.log(JSON.parse(ite.body).name);
      return JSON.parse(ite.body).name;
    });
  });
}
body();
