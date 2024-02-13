#!/usr/bin/node

/*
 * prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer
 * else prints "Not a number".
 */

const arg = process.argv[2];

if (isNaN(parseInt(arg))) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(arg));
}
