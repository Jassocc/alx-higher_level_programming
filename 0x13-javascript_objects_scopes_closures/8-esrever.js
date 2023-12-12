#!/usr/bin/node
exports.esrever = function (list) {
  const revList = [];
  let a;
  for (a = list.length - 1; a >= 0; a--) {
    revList[list.length - 1 - a] = list[a];
  }
  return (revList);
};
