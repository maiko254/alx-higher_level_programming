#!/usr/bin/node
if (process.argv.length > 2) {
  const intNum = parseInt(process.argv[2]);
  if (isNaN(intNum)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${intNum}`);
  }
} else {
  console.log('Not a number');
}
