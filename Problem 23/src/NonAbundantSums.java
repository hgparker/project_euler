import java.util.ArrayList;
import java.util.HashSet;

public class NonAbundantSums {

    private int nonAbundantSummableSum;

    public int getSum() {
        return nonAbundantSummableSum;
    }

    public NonAbundantSums() {
        nonAbundantSummableSum = 0;
        int capacity = 150;
        AbundantNumberGenerator generator = new AbundantNumberGenerator(capacity);

        for (int n = 1; n < 29000; n++) {
            if (n > capacity - 1) {
                generator.grow();
                capacity *= 2;
            }
            boolean summable = false;
            for (int index = 0; index < generator.abundantsList.size(); index++) {
                if (n < generator.abundantsList.get(index))
                    break;
                else if (generator.abundantsHash.contains(n - generator.abundantsList.get(index))) {
                    summable = true;
                    break;
                }
            }
            if (!summable)
                nonAbundantSummableSum += n;
        }
    }

    private class AbundantNumberGenerator {
        private int[] properDivisorSum;
        private ArrayList<Integer> primes;

        public ArrayList<Integer> abundantsList;
        public HashSet<Integer> abundantsHash;

        public AbundantNumberGenerator(int startingCapacity) {
            properDivisorSum = new int[startingCapacity];
            primes = new ArrayList<>();
            abundantsList = new ArrayList<>();
            abundantsHash = new HashSet<>();

            for (int k = 2; k < startingCapacity; k++)
                properDivisorSum[k] = 1;

            int primePower, numerator, denominator;

            for (int k = 2; k < startingCapacity; k++) {
                // if prime
                // or if abundant
                if (properDivisorSum[k] == 1) {
                    primes.add(k);

                    //find max power below startingCapacity
                    primePower = k;
                    denominator = k - 1;
                    while (primePower < startingCapacity) {
                        numerator = primePower * k - 1;

                        for (int p = 1; p * primePower < startingCapacity; p++) {
                            if (p % k != 0) {
                                properDivisorSum[p * primePower] *= numerator;
                                properDivisorSum[p * primePower] /= denominator;
                            }
                        }
                        primePower *= k;
                    }

                } else if (properDivisorSum[k] - k > k) {
                    abundantsList.add(k);
                    abundantsHash.add(k);
                }
            }
        }

        public void grow() {

            int oldCapacity = properDivisorSum.length;
            int newCapacity = properDivisorSum.length * 2;
            int[] biggerProper = new int[newCapacity];
            properDivisorSum = biggerProper;

            for (int k = oldCapacity; k < newCapacity; k++)
                properDivisorSum[k] = 1;

            // process old primes
            int primePower, numerator, denominator;
            for (int primeIndex = 0; primeIndex < primes.size(); primeIndex++) {

                int prime = primes.get(primeIndex);
                primePower = prime;
                denominator = prime - 1;

                while (primePower < newCapacity) {
                    numerator = primePower * prime - 1;

                    for (int p = (int) Math.ceil(oldCapacity / primePower);
                         p * primePower < newCapacity; p++) {

                        if (p % prime != 0) {
                            properDivisorSum[p * primePower] *= numerator;
                            properDivisorSum[p * primePower] /= denominator;
                        }
                    }
                    primePower *= prime;
                }
            }
            // the new hunt begins
            for (int k = oldCapacity; k < newCapacity; k++) {
                // if prime
                // or if abundant
                if (properDivisorSum[k] == 1)
                    primes.add(k);
                else if (properDivisorSum[k] - k > k) {
                    abundantsList.add(k);
                    abundantsHash.add(k);
                }
            }
        }
    }

    public static void main(String[] args) {
        NonAbundantSums test = new NonAbundantSums();
        System.out.println(test.getSum());
    }
}
