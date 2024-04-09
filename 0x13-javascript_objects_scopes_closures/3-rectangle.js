#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (arguments.length <= 1) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let result = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        result += 'x';
      }
      console.log(result);
      result = '';
    }
  }
}

module.exports = Rectangle;
