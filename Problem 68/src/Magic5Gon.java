public class Magic5Gon {
    // Helper functions help themselves to same global variables to avoid recalculating/copying
    // Thus, no arguments, and the hash must be "cleaned" from time to time
    // This code could easily be modified to work for Magic-n-gon

    private String maxSolution;
    private int[] centerValues;
    private int[] centerNext;
    private int centerStart;
    private boolean[] numbersUsed;
    private int magicSum;

    public String getMaxSolution() {
        return maxSolution;
    }

    //finish editing this code
    //Set centerStart correctly and calculate magicSum
    //Variables are all global
    //returns false if any pair-sum is the same
    private boolean findStart() {
        int runningSum = 0;

        //Looking for greatest sum of element + next
        for (int k = 0; k < 5; k++) {
            if (centerValues[k] + centerValues[centerNext[k]] > runningSum) {
                runningSum = centerValues[k] + centerValues[centerNext[k]];
                centerStart = k;
            } else if (centerValues[k] + centerValues[centerNext[k]] == runningSum)
                return false;
        }

        //Set magic sum
        int leastAvailable = 0;

        for (int k = 1; k < 11; k++) {
            if (!numbersUsed[k]) {
                leastAvailable = k;
                break;
            }
        }

        magicSum = leastAvailable + centerValues[centerStart] + centerValues[centerNext[centerStart]];

        return true;
    }

    // Updates maxSolution if the challenger solution is greater
    private void maxUpdate(String challenger) {
        long lChallenger = Long.parseLong(challenger);
        long lPresent = Long.parseLong(maxSolution);

        if (lChallenger > lPresent)
            maxSolution = challenger;
    }

    // tests if the proposed center-ordering generates a solution
    // doesn't take any arguments because it's just reading the global variables
    // returns false if doesn't work
    // if does work, automatically compares solution against best and updates
    private boolean testCenterOrdering() {

        int curr = centerStart;
        int currSpoke;
        int curr2;
        boolean status = true;

        do {
            // if we don't have the digit we need, then shut it down
            // if we do, then make it unavailable and advance

            currSpoke = magicSum - centerValues[curr] - centerValues[centerNext[curr]];
            if (currSpoke > 10 || numbersUsed[currSpoke]) {
                status = false;
                break;
            }

            numbersUsed[currSpoke] = true;
            curr = centerNext[curr];

        } while (curr != centerStart);

        // if we have a solution, record and update best
        if (status) {

            String challenger = "";
            curr = centerStart;

            do {
                currSpoke = magicSum - centerValues[curr] - centerValues[centerNext[curr]];
                challenger += Integer.toString(currSpoke) + Integer.toString(centerValues[curr]) +
                        Integer.toString(centerValues[centerNext[curr]]);

                curr = centerNext[curr];
            } while (curr != centerStart);

            //System.out.println(magicSum + " " + challenger);
            maxUpdate(challenger);
        }

        // Now clean hash
        if (!status)
            curr2 = centerStart;
        else {
            currSpoke = magicSum - centerValues[centerStart] - centerValues[centerNext[centerStart]];
            numbersUsed[currSpoke] = false;
            curr2 = centerNext[centerStart];
        }

        while (curr2 != curr) {
            currSpoke = magicSum - centerValues[curr2] - centerValues[centerNext[curr2]];
            numbersUsed[currSpoke] = false;
            curr2 = centerNext[curr2];
        }
        return status;
    }

    public Magic5Gon() {
        maxSolution = "0";

        centerValues = new int[5];
        centerNext = new int[5];
        centerStart = 0;
        numbersUsed = new boolean[11];
        magicSum = 0;

        for (int k = 0; k < 5; k++) {
            centerValues[k] = 0;
            centerNext[k] = 0;
            centerNext[k] = (k + 1) % 5;
        }

        for (int k = 1; k < 11; k++)
            numbersUsed[k] = false;

        // test every permutation of distinct digits with the smallest first
        // this ensures we try every distinct permutation of the five positions up to rotation
        // also, we never put 10 on the inside b/c that would yield 17 digits

        for (int a = 1; a < 6; a++) {
            centerValues[0] = a;
            numbersUsed[a] = true;

            for (int b = a + 1; b < 10; b++) {
                centerValues[1] = b;
                numbersUsed[b] = true;

                for (int c = a + 1; c < 10; c++) {

                    if (b == c)
                        continue;

                    centerValues[2] = c;
                    numbersUsed[c] = true;

                    for (int d = a + 1; d < 10; d++) {

                        if (d == b || d == c)
                            continue;

                        centerValues[3] = d;
                        numbersUsed[d] = true;

                        for (int e = a + 1; e < 10; e++) {

                            if (e == b || e == c || e == d)
                                continue;

                            centerValues[4] = e;
                            numbersUsed[e] = true;

                            // test helper will also remember solution and update max if necc
                            if (findStart())
                                testCenterOrdering();

                            //Clean hash
                            numbersUsed[e] = false;
                        }
                        //Clean hash
                        numbersUsed[d] = false;
                    }
                    //Clean hash
                    numbersUsed[c] = false;
                }
                //Clean hash
                numbersUsed[b] = false;
            }
            //Clean hash
            numbersUsed[a] = false;
        }
    }

    public static void main(String[] args) {
        Magic5Gon m5g = new Magic5Gon();
        System.out.println(m5g.getMaxSolution());
    }
}
