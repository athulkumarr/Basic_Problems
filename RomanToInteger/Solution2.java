class Solution2 {
    public static void main(String args[]) {
        System.out.println(romanToInt("MCMXCIV"));
    }
    public int romanToInt(String s) {
        HashMap<Character, Integer> romanToIntegerValues = new HashMap<>();
        romanToIntegerValues.put('I',1);
        romanToIntegerValues.put('V',5);
        romanToIntegerValues.put('X',10);
        romanToIntegerValues.put('L',50);
        romanToIntegerValues.put('C',100);
        romanToIntegerValues.put('D',500);
        romanToIntegerValues.put('M',1000);

        int integerValue = 0;

        for(int i = 0; i < s.length(); i++) {
            if(i < (s.length()-1) && romanToIntegerValues.get(s.charAt(i)) < romanToIntegerValues.get(s.charAt(i+1))) {
                integerValue -= romanToIntegerValues.get(s.charAt(i));
            } else {
                integerValue += romanToIntegerValues.get(s.charAt(i));
            }
        }
        romanToIntegerValues.clear();
        return integerValue;
    }
}
