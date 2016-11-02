// Author: Alexandre Brilhante

/* Return true if s is a palindrome. */

def palindrome(s: String): Boolean = {
  if (s.length <= 1) true
  else if (s.head != s.last) false
  else palindrome(s.substring(1, s.length - 1))
}
