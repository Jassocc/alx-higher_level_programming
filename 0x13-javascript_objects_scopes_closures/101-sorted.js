#!/usr/bin/node
const data = require('./101-data');
const origDict = data.dict;
const newDict = {};
for (const userId in origDict) {
  const occur = origDict[userId];
  if (!(occur in newDict)) {
    newDict[occur] = [];
  }
  newDict[occur].push(userId);
}
console.log(newDict);
