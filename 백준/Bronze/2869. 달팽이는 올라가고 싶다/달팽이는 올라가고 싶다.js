const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim();

const [A, B, V] = input.split(' ').map(Number);
const dailyClimb = A - B;
const days = Math.ceil((V - A) / dailyClimb) + 1;
console.log(days);