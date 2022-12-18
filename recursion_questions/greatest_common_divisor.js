function gcd(a, b) {
  if (b === 0) {
    return a;
  }
  return gcd(b, a % b);
}

console.log(gcd(8, 12));
console.log(gcd(12, 24));
console.log(gcd(1, 7));
