public class Problem4 {
    static boolean isPalindrome(int number) {
        String str = Integer.toString(number);

        int len = str.length();
        int m, n;
        m = 0;
        n = len - 1;

        while (m < n) {
            if (str.charAt(m) != str.charAt(n))
                return false;
            m++;
            n--;
        }
        return true;
    }

    public static void main(String[] args) {

        int max = 0;

        for (int k = 999; k >= 100; k--) {
            for (int m = k; m >= 100; m--) {
                if (isPalindrome(k * m))
                    if (k * m > max)
                        max = k * m;
            }
        }
        System.out.print(max + "\n");
    }
}
