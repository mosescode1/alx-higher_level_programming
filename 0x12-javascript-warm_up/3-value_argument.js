#!/usr/bin/node
const cmdLineArgv = process.argv;
if (cmdLineArgv.length === 2) {
  console.log('No argument');
} else {
  console.log(cmdLineArgv[2]);
}
