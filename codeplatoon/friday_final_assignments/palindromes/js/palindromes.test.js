 const palindrome = require("./palindrome")

 test('racecar is a truthy', () => {
   const result = palindrome("racecar")
   expect(result).toBeTruthy;
 })

 test('racecar is a truthy', () => {
  const result = palindrome("racecar")
  expect(result).toBe(true);
})