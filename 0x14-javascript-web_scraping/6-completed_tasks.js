#!/usr/bin/node
const request = require('request');
const apiURL = process.argv[2];
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    process.exit(1);
  }
  const tasks = JSON.parse(body);
  const completedTask = tasks.filter(task => task.completed);
  const completedCount = completedTask.reduce((acc, task) => {
    acc[task.userId] = (acc[task.userId] || 0) + 1;
    return acc;
  }, {});
  console.log(completedCount);
});
