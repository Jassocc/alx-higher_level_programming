#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const occCount = list.reduce((count, element) => {
    if (element === searchElement) {
      count++;
    }
    return (count);
  }, 0);
  return (occCount);
};
