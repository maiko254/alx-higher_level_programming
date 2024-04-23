#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, { json: true }, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const completedTasks = {};
  body.forEach(task => {
    if (task.completed) {
      completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
    }
  });
  JSON.stringify(completedTasks);
  console.log(completedTasks);
});
