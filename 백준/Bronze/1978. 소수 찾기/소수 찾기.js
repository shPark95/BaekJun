const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const T = input[0];
const N = input[1].split(' ').map(Number);

const max = Math.max(...N)
const isPrime = new Array(max + 1).fill(true);
isPrime[0] = isPrime[1] = false;


for (let i = 2; i * i <= max; i++) {
    if (isPrime[i]) {
        for (let j = i * i; j <= max; j += i) {
            isPrime[j] = false;
        }
    }
}

let result = 0;
for (let number of N) {
    if (isPrime[number]) {
        result += 1;
    }
}

console.log(result);