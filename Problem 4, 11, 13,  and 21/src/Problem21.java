public class Problem21 {

    public static void main(String[] args) {
        int n = 10000;
        int divisorSums[] = new int[n];

        for (int k = 0; k < n; k++)
            divisorSums[k] = 0;

        int divisorLimit = n / 2 + 1;
        for (int d = 1; d < divisorLimit; d++) {
            for (int k = 2 * d; k < n; k += d) {
                divisorSums[k] += d;
            }
        }

        int amicableSum = 0;

        for (int k = 1; k < n; k++) {
            if (divisorSums[k] < n && divisorSums[divisorSums[k]] == k && divisorSums[k] != k)
                amicableSum += k;
        }

//        for (int k = 1; k < n; k++)
        //          System.out.println(k + " " + divisorSums[k]);

        System.out.println(divisorSums[284]);
        System.out.println(amicableSum);
    }
}
