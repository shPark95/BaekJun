const fs = require('fs');
const [A, B] = fs.readFileSync(0, 'utf-8').trim().split('\n')

const a = Number(A);

for (let i = B.length - 1; i >= 0; i--) {
    const b = Number(B[i]);
    console.log(a * b);
}

console.log(a * Number(B));
