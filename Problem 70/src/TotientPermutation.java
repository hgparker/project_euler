public class TotientPermutation {

    int[] phi;

    public TotientPermutation(int limit) {
        phi = new int[limit];


        for (int k = 1; k < limit; k++)
            phi[k] = k;

        // purely to set a floor
        int min = -1;
        double minRatio = 500;
        double ratio;

        for (int k = 2; k < limit; k++) {
            //if k is prime, set to adjust all multiples, including k itself
            if (phi[k] == k) {
                for (int p = k; p < limit; p += k)
                    phi[p] = (phi[p] / k) * (k - 1);
            }

            ratio = ((double) k) / phi[k];
            if (ratio < minRatio) {
                if (isPermutation(k, phi[k])) {
                    min = k;
                    minRatio = ratio;
                }
            }
        }
        System.out.println(min);
    }


    //is num2 a permutation of num1 (order is actually important...see bit about 0)
    private boolean isPermutation(int num1, int num2) {

        if ((num1 - num2) % 9 != 0)
            return false;

        int[] digitHash1 = new int[10];
        int[] digitHash2 = new int[10];

        int x = num1;
        while (x > 0) {
            digitHash1[(x % 10)]++;
            x /= 10;
        }

        x = num2;
        while (x > 0) {
            digitHash2[(x % 10)]++;
            x /= 10;
        }

        if (digitHash2[0] > digitHash1[0])
            return false;

        for (int k = 1; k < 10; k++) {
            if (digitHash1[k] != digitHash2[k])
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        int limit = Integer.parseInt(args[0]);
        TotientPermutation test = new TotientPermutation(limit);
    }
}
