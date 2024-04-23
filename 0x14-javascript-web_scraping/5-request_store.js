#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: node get_webpage_content.js <url> <file_path>');
  process.exit(1);
}

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to fetch webpage. Status code:', response.statusCode);
  } else {
    fs.writeFile(filePath, body, { encoding: 'utf8' }, (err) => {
      if (err) {
        console.error('Error writing to file:', err);
      }
    });
  }
});
