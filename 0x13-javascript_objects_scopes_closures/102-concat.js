#!/usr/bin/node
const fs = require('fs');
const [, , fileA, fileB, destination] = process.argv;
const contA = fs.readFileSync(fileA, 'utf-8');
const contB = fs.readFileSync(fileB, 'utf-8');
const concatedfile = contA + contB;
fs.writeFileSync(destination, concatedfile);
