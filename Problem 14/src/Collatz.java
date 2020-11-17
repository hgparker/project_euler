public class Collatz {

    public static int Collatz1_helper(long n) {

        int count = 0;
        while (n != 1) {
            if (n % 2 == 0)
                n /= 2;
            else
                n = 3 * n + 1;
            count++;
        }
        return count;
    }

    public static int Collatz1(int limit) {
        int maxCollatz = 0;
        int maxStart = 1;
        int collatzCount = 0;

        for (int k = 1; k < limit; k++) {
            collatzCount = Collatz1_helper(k);
            if (collatzCount > maxCollatz) {
                maxCollatz = collatzCount;
                maxStart = k;
            }
        }

        return maxStart;
    }

    public static void main(String[] args) {
        int limit = Integer.parseInt(args[0]);

        System.out.println(Collatz1(limit));
    }
}
