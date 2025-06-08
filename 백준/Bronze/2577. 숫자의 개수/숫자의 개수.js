const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const result = input[0] * input[1] * input[2];

const digits = result.toString().split('').map(Number);
const count = Array(10).fill(0);
for (const digit of digits) {
    count[digit]++;
}
console.log(count.join('\n'));


