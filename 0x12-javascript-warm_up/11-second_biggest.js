#!/usr/bin/node
function findSecondLargest (nums) {
  if (nums.length < 2) {
    return (0);
  }
  nums = nums.map(Number);
  const max = Math.max.apply(null, nums);
  nums = nums.filter(num => num !== max);
  return Math.max.apply(null, nums);
}
const args = process.argv.slice(2);
console.log(findSecondLargest(args));
