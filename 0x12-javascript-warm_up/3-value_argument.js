#!/usr/bin/python3
const argument = process.argv;
if (argument[2] !== undefined) {
 console.log(argument[2]);
} else {
  console.log('No argument');
}
