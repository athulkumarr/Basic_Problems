class Solution {
    public static void main(String args[])
    {
        intToRoman(3499);
    }
  
    public void intToRoman(int num) 
    {
        String numStr = String.valueOf(num);
        StringBuilder roman = new StringBuilder();
        String[] lettersbefore5 = {"I", "X", "C","M"};
        String[] lettersafter5 = {"V", "L", "D"};
        int n = numStr.length();

        for(int i = 0; i < n; i++)
        {
            switch(numStr.charAt(i))
            {
                case '1':
                    roman.append(lettersbefore5[n-i-1]);
                    break;
                case '2':
                    roman.append(lettersbefore5[n-i-1]+lettersbefore5[n-i-1]);
                    break;
                case '3':
                    roman.append(lettersbefore5[n-i-1]+lettersbefore5[n-i-1]+lettersbefore5[n-i-1]);
                    break;
                case '4':
                    roman.append(lettersbefore5[n-i-1]+lettersafter5[n-i-1]);
                    break;
                case '5':
                    roman.append(lettersafter5[n-i-1]);
                    break;
                case '6':
                    roman.append(lettersafter5[n-i-1]+lettersbefore5[n-i-1]);
                    break;
                case '7':
                    roman.append(lettersafter5[n-i-1]+lettersbefore5[n-i-1]+lettersbefore5[n-i-1]);
                    break;
                case '8':
                    roman.append(lettersafter5[n-i-1]+lettersbefore5[n-i-1]+lettersbefore5[n-i-1]+lettersbefore5[n-i-1]);
                    break;
                case '9':
                    roman.append(lettersbefore5[n-i-1]+lettersbefore5[n-i]);
                    break;
            }
        }
        System.out.println(roman.toString());
    }
}
