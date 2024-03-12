#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w !== 0 && w > 0 && h !== 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      for (let r = 0; r < this.width; r++) {
        process.stdout.write('X');
        if (r === this.width - 1) {
          console.log();
        }
      }
    }
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
