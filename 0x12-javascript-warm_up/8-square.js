#!/usr/bin/node

/*
 * Prints a square.
 */
const input = process.argv[2];
let i = 1;

if (isNaN(parseInt(input))) {
  console.log('Missing size');
} else {
  while (i <= input) {
    console.log('X'.repeat(input));
    i++;
  }
}
