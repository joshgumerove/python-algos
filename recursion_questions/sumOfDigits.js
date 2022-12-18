function sumOfDigits(n) {
  if (n < 10) {
    return n;
  }
  return (n % 10) + sumOfDigits(parseInt(n / 10));
}

console.log(sumOfDigits(22));
console.log(sumOfDigits(7));
console.log(sumOfDigits(222));
