const getCount = str => { return (str.match(/[aouei]/g) || []).length;}

console.log(getCount("aabbcaaceedd"));