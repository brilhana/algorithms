// Author: Alexandre Brilhante

/* Returns an integer in Roman numeral representation. */

var roman = function (n) {
  return number(n, 1000, "M", "", "")+number(n, 100, "C", "D", "M")+number(n, 10, "X", "L", "C")+number(n, 1, "I", "V", "X");
};

var number = function (n, base, one, five, ten) {
  var c = Math.floor(n/base)%10;
  if (c < 4) {
    return repeat(c, one);
  }
  else if (c == 4) {
    return one+five;
  }
  else if (c < 9) {
    return five+repeat(c-5, one);
  }
  else {
    return one+ten;
  }
};

var repeat = function (n, value) {
    var temp = "";
    for (var i = n; i > 0; i--) {
        temp += value;
    }
    return temp;
};

var test = function () {
    assert(repeat(0, "I")                  == "");
    assert(repeat(3, "I")                  == "III");
    assert(number(439, 1, "I", "V", "X")   == "IX");
    assert(number(439, 10, "X", "L", "C")  == "XXX");
    assert(number(439, 100, "C", "D", "M") == "CD");
    assert(number(439, 1000, "M", "", "")  == "");
    assert(roman(1)                        == "I");
    assert(roman(3)                        == "III");
    assert(roman(4)                        == "IV");
    assert(roman(5)                        == "V");
    assert(roman(8)                        == "VIII");
    assert(roman(9)                        == "IX");
    assert(roman(10)                       == "X");
    assert(roman(627)                      == "DCXXVII");
    assert(roman(3948)                     == "MMMCMXLVIII");
    assert(roman(3999)                     == "MMMCMXCIX");
};

test();
