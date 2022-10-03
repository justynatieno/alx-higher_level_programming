#!/usr/bin/node
const argument = parseInt(process.argv[2]);
if (Number.isNaN(argument)) {
  console.log('Missing number of occurences');
} else {
  for (let x = 0; x < argument; x++) {
    console.log('C is fun');
  }
}
