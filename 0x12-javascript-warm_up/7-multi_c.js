#!/usr/bin/node
if (process.argv.length > 2) {
  const x = parseInt(process.argv[2]);
  if (isNaN(x)) {
    prnt('Missing number of occurrences');
  } else {
    let i = 0;
    while (i < x) {
      console.log('C is fun');
      i++;
    }
  }
} else {
  prnt('Missing number of occurrences');
}

function prnt (str) {
  console.log(str);
}
