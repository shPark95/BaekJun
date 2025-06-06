const fs = require('fs');
const year = parseInt(fs.readFileSync(0, 'utf-8').trim(), 10);

if ((year % 4 === 0 && year % 100 !== 0) || year % 400 === 0) {
    console.log(1);
} else {
  console.log(0);
}