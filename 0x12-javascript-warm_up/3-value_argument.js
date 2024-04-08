#!/usr/bin/node
const cmdLineArgv = process.argv;

function arrayLength(array) {
  let count = 0;
  for (let elem in array) {
    count++;
  }
  return count;
}
let arrayCount = arrayLength(cmdLineArgv);
if (arrayCount === 2) {
  console.log('No argument');
} else {
  console.log(cmdLineArgv[2]);
}
