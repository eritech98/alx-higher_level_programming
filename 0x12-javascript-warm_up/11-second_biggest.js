#!/usr/bin/node

/*
 * Searches the second biggest integer in the list of arguments.
 */

const input = process.argv;
let big = parseInt(input[2]);
let second = 0;
let i = 2;

while (i < input.length && input.length !== 3) {
  if (parseInt(input[i]) > big) {
    second = big;
    big = parseInt(input[i]);
  }
  if (parseInt(input[i]) < big && parseInt(input[i]) > second) {
    second = parseInt(input[i]);
  }
  i++;
}

console.log(second);
