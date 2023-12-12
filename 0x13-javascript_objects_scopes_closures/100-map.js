#!/usr/bin/node
const data = require('./100-data');
const initList = data.list;
const newList = initList.map((value, index) => value * index);
console.log(initList);
console.log(newList);
