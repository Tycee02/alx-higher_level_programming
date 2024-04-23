#!/usr/bin/node

const fs = require('fs');

const writeStringToFile = (filePath, cotent) => {
  fs.writeFile(filePath, content, { encoding: 'utf8' }, (err) => {
    if (err) {
      console.error('An error occured:', err);
    }
  });
};

if (process.argv.length !== 4) {
  console.error('Usage: node read_file.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];
writeStringToFile(filePath);
