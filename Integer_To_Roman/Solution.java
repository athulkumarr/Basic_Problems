class Solution {
  public static void main(Sring args[])
  {
    intToRoman(2989);  
  }
  public void intToRoman(int num) {
    final int[] integers = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    final String[] romans = {"M",  "CM", "D",  "CD", "C",  "XC", "L",
                              "XL", "X",  "IX", "V",  "IV", "I"};
    StringBuilder sb = new StringBuilder();

    for (int i = 0; i < integers.length; ++i) {
      if (num == 0)
        break;
      while (num >= integers[i]) {
        num -= integers[i];
        sb.append(romans[i]);
      }
    }
    System.out.println(sb.toString());
  }
}
