class Solution {
    public static int minNumberOfFrogs(String croakOfFrogs) {
        int c = 0, r = 0, o = 0, a = 0, k = 0, maxFrogs = 0;
        for(int i = 0; i < croakOfFrogs.length(); i++) {
            char ch = croakOfFrogs.charAt(i);
            switch(ch) {
                case 'c':
                    c++;
                    maxFrogs  = (c-k) > maxFrogs? c-k : maxFrogs;
                    break;
                case 'r':
                    r++;
                    if(r>c) 
                        return -1;
                    break;
                case 'o':
                    o++;
                    if(o>r) 
                        return -1;
                    break;
                case 'a':
                    a++;
                    if(a>o) 
                        return -1;
                    break;
                case 'k':
                    k++;
                    if(k>a) 
                        return -1;
                    break;
            }
        }
        if(c!=r || r!=o || o!=a || a!=k) {
            return -1;
        }
        return maxFrogs;
    }
    
    public static void main(String args[]) {
        System.out.println(minNumberOfFrogs("croakcroakccroaroakk"));
    }
}
