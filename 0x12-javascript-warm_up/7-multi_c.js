#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!isNaN(x)) {
  let a;
  for (a = 0; a < x; a++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
