class Solution {
    public static void main(String args[]) {
      System.out.println(isPalindrome(121)?"True":"False");
    }
    public static boolean isPalindrome(int x) {
        if((x < 0) || (x != 0 && x%10 == 0)){
            return false;
        }
        int half = 0;
        while(x>half) {
            half = half*10 + x%10;
            x = x/10;
        }
        return ((half == x) || (half/10 == x));
    }
}
