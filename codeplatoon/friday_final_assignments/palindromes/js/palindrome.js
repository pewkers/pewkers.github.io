const palindrome = (word) => {
  let solution = false;
  word = word.toLowerCase().replace(/[^a-z0-9]/g, '')

  if (word === word.split("").reverse().join("")) {
    solution = true;
  }

  console.log(solution)
  return solution;

};

// palindrome("racecar");
// palindrome("Noon");
// palindrome("ciVic");
// palindrome("nice");
// palindrome("434");
// palindrome("123");

// palindrome("Sore was I ere I saw Eros.");
// palindrome("A man, a plan, a canal -- Panama");

module.exports = palindrome;