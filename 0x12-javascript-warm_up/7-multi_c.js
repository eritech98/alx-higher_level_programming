#!/usr/bin/node

/*
 * Prints x times “C is fun”.
 */

let i = 1;

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  while (i <= parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
}
