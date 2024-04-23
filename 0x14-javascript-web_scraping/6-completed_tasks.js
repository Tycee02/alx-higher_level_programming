#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node count_completed_tasks.js <api_url>');
  process.exit(1);
}

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch task list. Status code:', response.statusCode);
  } else {
    try {
      const tasks = JSON.parse(body);
      const completedTasksByUser = {};

      tasks.forEach((task) => {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error('Error parsing response:', parseError);
    }
  }
});
