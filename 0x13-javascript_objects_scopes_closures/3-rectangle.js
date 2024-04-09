#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (arguments.length <= 1) {
      return;
    }
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('x'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
