#!/usr/bin/node
function callMeMoby(num, func) {
  for (i = 0; i < num; i++) {
    func();
  }
}

module.exports = { callMeMoby };
