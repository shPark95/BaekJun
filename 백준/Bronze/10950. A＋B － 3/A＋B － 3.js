const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const T = parseInt(input[0]);

for (let i = 0; i < T; i++) {
    const [A, B] = input[i + 1].split(' ').map(Number);
    console.log(A + B);
}