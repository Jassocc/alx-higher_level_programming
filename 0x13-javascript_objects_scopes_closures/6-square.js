#!/usr/bin/node
const bSquare = require('./5-square');
class Square extends bSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let a;
    for (a = 0; a < this.height; a++) {
      console.log(c.repeat(this.height));
    }
  }
}
module.exports = Square;
