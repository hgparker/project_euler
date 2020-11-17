public class Problem11 {

/*    public static int FactorCount(long x) {
        // Simplest possible algorithm...linear time on x
        int count = 1;

        if (x > 1)
            count++;

        for (int k = 2; k < x / 2 + 1; k++) {
            if (x % k == 0)
                count++;
        }
        return count;
    } */

    public static int FancyFactorCount(long x) {
        // Fancier algo...uses prime factorization...runs in time proportional to largest prime factor
        // Malfunctions for very, very large numbers...not sure why??

        if (x == 1)
            return 1;

        int count = 1;
        long xlimit = (long) Math.sqrt(x) + 1;
        int tempcount = 0;

        for (int k = 2; k < xlimit; k++) {
            if (x % k == 0) {
                tempcount = 1;
                x = x / k;
                while (x >= k && x % k == 0) {
                    tempcount++;
                    x = x / k;
                }
                count *= tempcount + 1;
                xlimit = (long) Math.sqrt(x) + 1;
            }
        }

        //If last factor is a prime
        if (x != 1)
            count *= 2;

        return count;
    }

    public static long GenerateTriangular(int n) {
        long l = (long) n;
        return (l * (l + 1)) / 2;
    }

/*    public static int SimpleSieveFactorFind(int maxSieveSize, int limit) {
        // Increments for every divisor...sieve-like, but with nothing else

        short divisorCount[] = new short[maxSieveSize];

        for (int k = 0; k < maxSieveSize; k++)
            divisorCount[k] = 1;

        for (int k = 2; k < maxSieveSize; k++) {
            for (int p = k; p < maxSieveSize; p += k) {
                divisorCount[p]++;
            }
            if (divisorCount[k] > limit)
                return k;
        }
        return -1;
    } */

    public static int FancySieveFactorFind(int maxSieveSize, int limit) {

        long divisorCount[] = new long[maxSieveSize];

        int p = 0, pDelta = 0;
        long pStop = 0;
        int m;
        long numFacsTri;

        for (int k = 0; k < maxSieveSize; k++)
            divisorCount[k] = 1;


        for (int k = 2; k < maxSieveSize; k++) {
            // if it's not a prime, we don't care
            // the k<limit thing needs to be proved... ditto w/ other limit idea you were tossing around
            if (k < 500 && divisorCount[k] == 1) {
                //what is greatest power of k we have to worry about?
                p = 0;
                while (Math.pow(k, p) < maxSieveSize) {
                    p++;
                }
                p--;
                pDelta = (int) Math.pow(k, p);
                pStop = pDelta * (long) k;

                while (p > 0) {
                    // divisorcount of every multiple of k^p should be multiplied by (p+1)
                    for (int q = pDelta; q < maxSieveSize; q += pDelta) {
                        if (q % (pStop) != 0) {
                            divisorCount[q] *= p + 1;
                        }
                    }
                    p--;
                    pDelta /= k;
                    pStop /= k;
                }
            }

            m = k - 1;

            if (m % 2 == 0)
                numFacsTri = divisorCount[m / 2] * divisorCount[m + 1];
            else
                numFacsTri = divisorCount[m] * divisorCount[(m + 1) / 2];

            if (numFacsTri > limit) {
                System.out.println("Tri-# " + m + " which is " + GenerateTriangular(m)
                        + " with " + numFacsTri + " factors.");
                return m;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int maxSieve = Integer.parseInt(args[0]);
        int limit = Integer.parseInt(args[1]);

        int k = FancySieveFactorFind(maxSieve, limit);

        System.out.println("FancySieve yields tri-number " + k +
                " which is " + GenerateTriangular(k) + " with alt-facs "
                + FancyFactorCount(GenerateTriangular(k)));
        /*
        int k = 1;
        int[] numFacs = new int[100000000];
        int numFacsTri;
        numFacs[1] = FancyFactorCount(1);
        numFacs[2] = FancyFactorCount(2);
        numFacsTri = numFacs[1] * numFacs[1];
        while (numFacsTri <= limit) {
            k++;
            numFacs[k + 1] = FancyFactorCount(k + 1);
            if (k % 2 == 0)
                numFacsTri = numFacs[k / 2] * numFacs[k + 1];
            else
                numFacsTri = numFacs[k] * numFacs[(k + 1) / 2];
        }

        System.out.println("Tri-number " + k + " which is " + GenerateTriangular(k) + " with facs " + numFacsTri);
        */
    }
}
