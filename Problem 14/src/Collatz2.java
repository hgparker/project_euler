public class Collatz2 {
    int[] count;
    int maxIndex;

    public int getMaxIndex() {
        return maxIndex;
    }

    public Collatz2(int maxLimit, int limit) {
        count = new int[maxLimit];
        long n;
        int runCount;
        int m;

        for (int k = 0; k < maxLimit; k++)
            count[k] = 0;

        count[1] = 1;
        maxIndex = 1;

        // Calculate every Collatz score <limit
        for (int k = 1; k < limit; k++) {
            n = k;
            runCount = 0;
            while (true) {
                if (n < maxLimit && count[(int) n] != 0) {
                    runCount += count[(int) n];
                    break;
                }

                if (n % 2 == 0)
                    n /= 2;
                else
                    n = 3 * n + 1;
                runCount++;
            }

            count[k] = runCount;
            if (count[k] > count[maxIndex])
                maxIndex = k;

            // handle all produts of 2^m < limit
            // make this a switch!
            // incorporate even stuff too

            switch (k % 6) {
                case 0:
                case 2:
                case 4:
                    break;

                case 1:
                    for (m = 2 * k; m < maxLimit; m *= 2)
                        count[m] = count[m / 2] + 1;

                    for (m = 4 * k; m < maxLimit; m *= 4)
                        count[(m - 1) / 3] = count[m] + 1;

                    break;

                case 3:

                    for (m = 2 * k; m < maxLimit; m *= 2)
                        count[m] = count[m / 2] + 1;

                    break;

                case 5:
                    for (m = 2 * k; m < maxLimit; m *= 2)
                        count[m] = count[m / 2] + 1;

                    for (m = 8 * k; m < maxLimit; m *= 4)
                        count[(m - 1) / 3] = count[m] + 1;

                    break;
            }
            /*
            if (k % 6 == 1) {
                for (m = 2 * k; m < maxLimit; m *= 2)
                    count[m] = count[m / 2] + 1;

                for (m = 4 * k; m < maxLimit; m *= 4)
                    count[(m - 1) / 3] = count[m] + 1;
            } else if (k % 6 == 3) {
                for (m = 2 * k; m < maxLimit; m *= 2)
                    count[m] = count[m / 2] + 1;
            } else if (k % 6 == 5) {
                for (m = 2 * k; m < maxLimit; m *= 2)
                    count[m] = count[m / 2] + 1;

                for (m = 8 * k; m < maxLimit; m *= 4)
                    count[(m - 1) / 3] = count[m] + 1;
            } */
        }
    }

    public static void main(String[] args) {
        int maxLimit = Integer.parseInt(args[0]);
        int limit = maxLimit;

        Collatz2 c = new Collatz2(maxLimit, limit);
        System.out.println(c.getMaxIndex());
    }
}
