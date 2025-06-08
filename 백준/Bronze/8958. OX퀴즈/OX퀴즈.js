const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const T = parseInt(input[0]);
const result = [];

for (let i = 1; i <= T; i++) {
    let score = 0;
    let count = 0;
    for (let j = 0; j < input[i].length; j++) {
        if (input[i][j] === 'O') {
            count += 1;
            score += count;
        } else {
            count = 0;
        }
    }
    result.push(score);
}

console.log(result.join('\n'));