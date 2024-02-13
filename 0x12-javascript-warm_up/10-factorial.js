#!/usr/bin/node

/*
 * Computes and prints a factorial.
 */

const num = parseInt(process.argv[2]);

function factorial (num) {
  /*
   * Computes the factorial of given input.
   */

  if (!num || num <= 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}

console.log(factorial(num));
