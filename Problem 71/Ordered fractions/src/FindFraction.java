public class FindFraction {

    public static int getNumerator(int d) {
        int n = (3 * d) / 7;
        if (3 * d == 7 * n)
            n--;
        return n;
    }

    public static boolean reducible(int n, int d) {
        for (int x = 2; x * x <= Math.min(n, d); x++) {
            if (n % x == 0 && d % x == 0)
                return true;
            while (n % x == 0)
                n /= x;
            while (d % x == 0)
                d /= x;
        }
        return ((n > 1) && (d % n == 0)) || ((d > 1) && (n % d == 0));
    }

    public static boolean greaterThan(int nA, int dA, int nB, int dB) {
        return (nA * dB) > (nB * dA);
    }

    public static void main(String[] args) {
//        System.out.println(getNumerator(Integer.parseInt(args[0])));
//        System.out.println(reducible(Integer.parseInt(args[0]), Integer.parseInt(args[1])));
        int bestN = 0;
        int bestD = 1;

        for (int d = 1; d <= 100000000; d++) {
            int n = getNumerator(d);
//            System.out.println("Checking " + n + " / ");
//            if (reducible(n, d)) continue;
            if (greaterThan(n, d, bestN, bestD)) {
//                System.out.println("Updating " + n + " / " + d);
                bestN = n;
                bestD = d;
            }
        }
        System.out.println("Infimum of 3/7 was " + bestN + " / " + bestD);
    }
}
