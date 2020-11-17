public class Magic3Gon {
    // In general, the helper functions all make use of the same global variables
    // to avoid unnecessary recalculating and copying
    // the center is stored as a circular linked list

    private String maxSolution;
    private int[] centerValues;
    private int[] centerNext;
    private int centerStart;
    private boolean[] numbersUsed;
    private int magicSum;

    public String getMaxSolution() {
        return maxSolution;
    }

    //Set center start correctly and calculate magicSum
    //Variables are all global
    //returns false if any pair-sum is the same
    private boolean findStart() {
        int runningSum = 0;

        //Looking for greatest sum of element + next
        for (int k = 0; k < 3; k++) {
            if (centerValues[k] + centerValues[centerNext[k]] > runningSum) {
                runningSum = centerValues[k] + centerValues[centerNext[k]];
                centerStart = k;
            } else if (centerValues[k] + centerValues[centerNext[k]] == runningSum)
                return false;
        }

        //Set magic sum
        int leastAvailable = 0;

        for (int k = 1; k < 7; k++) {
            if (!numbersUsed[k]) {
                leastAvailable = k;
                break;
            }
        }

        magicSum = leastAvailable + centerValues[centerStart] + centerValues[centerNext[centerStart]];
        return true;
    }

    // Updates maxSolution if the challenger solution  is greater
    private void maxUpdate(String challenger) {
        long lChallenger = Long.parseLong(challenger);
        long lPresent = Long.parseLong(maxSolution);

        if (lChallenger > lPresent)
            maxSolution = challenger;
    }

    // tests if the proposed center-ordering generates a solutions
    // doesn't take any arguments because it's just reading the global variables
    // returns false if doesn't work
    // if does work, automatically compares solution against best
    private boolean testCenterOrdering() {

        int curr = centerStart;
        int currSpoke;
        int curr2;
        boolean status = true;

        do {
            // if we don't have the digit we need, then shut it down
            // if we do, then make it unavailable and advance

            currSpoke = magicSum - centerValues[curr] - centerValues[centerNext[curr]];
            if (currSpoke > 6 || numbersUsed[currSpoke]) {
                status = false;
                break;
            }

            numbersUsed[currSpoke] = true;
            curr = centerNext[curr];

        } while (curr != centerStart);

        // if status is false, we need to clean the hash table
        if (status) {

            // Make solution into string & keep update
            String challenger = "";
            curr = centerStart;

            do {
                currSpoke = magicSum - centerValues[curr] - centerValues[centerNext[curr]];
                challenger += Integer.toString(currSpoke) + Integer.toString(centerValues[curr]) +
                        Integer.toString(centerValues[centerNext[curr]]);

                curr = centerNext[curr];
            } while (curr != centerStart);

            System.out.println(magicSum + " " + challenger);
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


    public Magic3Gon() {
        maxSolution = "0";

        centerValues = new int[3];
        centerNext = new int[3];
        centerStart = 0;
        numbersUsed = new boolean[7];
        magicSum = 0;

        for (int k = 0; k < 3; k++) {
            centerValues[k] = 0;
            centerNext[k] = 0;
            centerNext[k] = (k + 1) % 3;
        }

        for (int k = 1; k < 7; k++)
            numbersUsed[k] = false;
/*
        centerValues[0] = 1;
        centerValues[1] = 3;
        centerValues[2] = 5;

        numbersUsed[1] = true;
        numbersUsed[3] = true;
        numbersUsed[5] = true;

        System.out.println(findStart());
        System.out.println(magicSum);
        System.out.println(centerStart);
        System.out.println(testCenterOrdering()); */


        // test every permutation of distinct digits with the smallest first
        for (int k = 1; k < 5; k++) {
            centerValues[0] = k;
            numbersUsed[k] = true;

            for (int p = k + 1; p < 7; p++) {
                centerValues[1] = p;
                numbersUsed[p] = true;

                for (int z = k + 1; z < 7; z++) {

                    if (z == p)
                        continue;

                    centerValues[2] = z;
                    numbersUsed[z] = true;

                    // test helper will also remember solution and update max if necc
                    if (findStart())
                        testCenterOrdering();

                    //Clean hash
                    numbersUsed[z] = false;
                }
                //Clean hash
                numbersUsed[p] = false;
            }
            //Clean hash
            numbersUsed[k] = false;
        }
    }

    public static void main(String[] args) {
        Magic3Gon m3g = new Magic3Gon();
        System.out.println(m3g.getMaxSolution());
    }
}
