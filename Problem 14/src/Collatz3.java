import java.util.Stack;

public class Collatz3 {
    int[] count;
    int maxIndex;

    public int getMaxIndex() {
        return maxIndex;
    }

    public Collatz3(int maxLimit, int limit) {
        count = new int[maxLimit];
        long n;
        int runCount;
        Stack<Long> stack = new Stack<>();

        for (int k = 0; k < maxLimit; k++)
            count[k] = 0;

        count[1] = 1;
        count[2] = 2;
        maxIndex = 1;

        // Calculate every Collatz score <limit
        for (int k = 3; k < limit; k++) {
            n = k;
            runCount = 0;

            while (true) {
                if (n < maxLimit && count[(int) n] != 0) {
                    runCount += count[(int) n];
                    break;
                }

                stack.push(n);

                if (n % 2 == 0)
                    n /= 2;
                else
                    n = 3 * n + 1;

                runCount++;
            }

            count[k] = runCount;
            if (count[k] > count[maxIndex])
                maxIndex = k;

            runCount = count[(int) n] + 1;
            while (!stack.isEmpty()) {
                n = stack.pop();
                runCount++;
                if (n < maxLimit && n != k)
                    count[(int) n] = runCount;
            }
        }
    }

    public static void main(String[] args) {
        int maxLimit = Integer.parseInt(args[0]);
        int limit = maxLimit;

        Collatz3 c = new Collatz3(maxLimit, limit);
        System.out.println(c.getMaxIndex());
    }

}
