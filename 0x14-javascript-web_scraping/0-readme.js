#!/usr/bin/node

const fs = require('fs');

const readAndPrintFile = (filePath) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('An error occured:', err);
    } else {
      console.log(data);
    }
  });
};

if (process.argv.length !== 3) {
  console.error('Usage: node read_file.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFile(filePath);
