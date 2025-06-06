const fs = require('fs');
const score = fs.readFileSync(0, 'utf-8').trim()

const s = Number(score);

if (s >= 90) {
    console.log('A');
} else if (s >= 80) {
    console.log('B');
} 
else if (s >= 70) {
    console.log('C');
} 
else if (s >= 60) {
    console.log('D');
} 
else {
    console.log('F');
}