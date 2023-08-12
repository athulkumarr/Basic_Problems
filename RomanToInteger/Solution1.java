class Solution {
    public static void main(String args[]) {
      System.out.println(romanToInt("MCMXCIV"));
    }
  
    public static int romanToInt(String s) {

        HashMap<Character, Integer> romanToIntegerValues = new HashMap<>();
        romanToIntegerValues.put('I',1);
        romanToIntegerValues.put('V',5);
        romanToIntegerValues.put('X',10);
        romanToIntegerValues.put('L',50);
        romanToIntegerValues.put('C',100);
        romanToIntegerValues.put('D',500);
        romanToIntegerValues.put('M',1000);

        s = s.replace("IV", "IIII");
        s = s.replace("IX", "VIIII");
        s = s.replace("XL", "XXXX");
        s = s.replace("XC", "LXXXX");
        s = s.replace("CD", "CCCC");
        s = s.replace("CM", "DCCCC");

        int integerValue = 0;
        System.out.println(s);

        for(int i = 0; i < s.length(); i++) {
            integerValue += romanToIntegerValues.get(s.charAt(i));
        }

        return integerValue;
    }
}
