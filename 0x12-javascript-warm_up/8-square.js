#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  const row = 'X'.repeat(size);
  let a;
  for (a = 0; a < size; a++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
