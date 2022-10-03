#!/usr/bin/node
const argument = parseInt(process.argv[2]);
if (Number.isNaN(argument)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < argument; x++) {
    let row = '';
    for (let y = 0; y < argument; y++) {
      row += 'X';
    }
    console.log(row);
  }
}
