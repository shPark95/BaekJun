
const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim();

function isHansu(num) {
    const diff1 = Number(num[1]) - Number(num[0]);
    const diff2 = Number(num[2]) - Number(num[1]);
    if (diff1 !== diff2) {
        return false;
    }
    return true;
}

if (Number(input) < 100) {
  console.log(input);
} else {
    let result = 99;
    for (let i = 100; i <= Number(input); i++) {
        if (isHansu(String(i))) {
            result++;
        }
    }
    console.log(result);
}