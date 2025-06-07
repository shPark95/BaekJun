const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const [N, X] = input[0].split(' ').map(Number);
const A = input[1].split(' ').map(Number);

result = [];
for (let i of A) {
    if (i < X) {
        result.push(i);
    }
}

console.log(result.join(' '));