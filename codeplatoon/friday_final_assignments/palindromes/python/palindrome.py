def palindrome(word):
   solution = True
   word = word.lower()
   word = word.replace(" ", "").replace(".", "").replace(",", "").replace("-", "")

   for i in range(len(word)//2):
         if word[i] != word[-1-i]:
                 solution = False             
   print(solution)
   return solution


palindrome("racecar")
palindrome("Noon")
palindrome("ciVic")
palindrome("nice")
palindrome("434")
palindrome("123")

palindrome("Sore was I ere I saw Eros.")
palindrome("A man, a plan, a canal -- Panama")