#!/usr/bin/node
// Read and print file content

const fs = require('fs');

// Check if file path argument is provided
if (process.argv.length < 3) {
  console.log("Usage: ./script.js <file_path>");
  process.exit(1);
}

const filePath = process.argv[2];

// Read file content
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error("An error occurred while reading the file:", err);
  } else {
    console.log(data);
  }
});
