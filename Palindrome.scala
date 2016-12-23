// Author: Alexandre Brilhante

/* Returns true if the argument is a palindrome. */

object Palindrome {
  def main(args: Array[String]) {
    println(palindrome(args{0}))
  }

  def palindrome(s: String): Boolean = {
    if (s.length <= 1) true
    else if (s.head != s.last) false
    else palindrome(s.substring(1, s.length - 1))
  }
}