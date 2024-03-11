#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length <= 1) {
  console.log(0);
} else {
  let max = -Infinity;
  let secondMax = -Infinity;
  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > max) {
      secondMax = max;
      max = num;
    } else if (num > secondMax && num < max) {
      secondMax = num;
    }
  }
  console.log(secondMax);
}
