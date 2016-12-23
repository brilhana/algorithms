// Author: Alexandre Brilhante

/* Returns true if the argument is even, false if not, without using addition, substraction, multiplication, division or modulo. */

import scala.collection.mutable.ListBuffer

object Parity {
  def main(args: Array[String]) {
    println(parity(args{0}.toInt))
  }

  def parity(i: Int): Boolean = {
    var even = new ListBuffer[String]()
    var odd = new ListBuffer[String]()
    for (x <- 1 to i) {
      if (even.length == odd.length) even += ""
      else odd += ""
    }
    if (even.length == odd.length) true
    else false
  }
}