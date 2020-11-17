import java.util.PriorityQueue;

public class Collatz4 {
    private int maxStart;
    private int numUnderLim;
    private int limit;

    private class Node implements Comparable<Node> {
        public long number;
        public int collatzScore;
        public double distPlusHeuristic;

        private Node(long n, int newCollatzScore) {
            number = n;
            collatzScore = newCollatzScore;
            distPlusHeuristic = 10 * Math.log10(number) + collatzScore;
        }

        public int compareTo(Node node) {
            if (this.distPlusHeuristic < node.distPlusHeuristic)
                return -1;
            else if (this.distPlusHeuristic > node.distPlusHeuristic)
                return 1;
            else
                return 0;

/*            if (this.number < node.number)
                return -1;
            else if (this.number > node.number)
                return 1;
            else
                return 0; */
        }
    }

    public Collatz4(int requestedLimit) {

        limit = requestedLimit;

        // Annoying small numbers
        if (limit <= 2) {
            maxStart = limit;
            return;
        }

        // Set up PQ
        PriorityQueue<Node> pq = new PriorityQueue<>();
        Node initialNode = new Node(8, 4);
        pq.add(initialNode);
        maxStart = 2;
        int maxScore = 2;
        long tempCount;
        int tempScore;
        numUnderLim = 3;

        // Keep running PQ
        Node curr, child, nchild;

        while (numUnderLim < limit - 1) {
            curr = pq.poll();

//            System.out.println("Processing " + curr.number + " with score " + curr.collatzScore);

            //handle curr in its own right
            if (curr.number < limit) {
                numUnderLim++;

                if (curr.collatzScore > maxScore) {
                    maxScore = curr.collatzScore;
                    maxStart = (int) curr.number;
                }
            }

            child = new Node(curr.number * 2, curr.collatzScore + 1);
            pq.add(child);
            //          System.out.println("---adding to pq " + child.number);

            if (curr.number % 6 == 4) {
                child = new Node((curr.number - 1) / 3, curr.collatzScore + 1);
                pq.add(child);
                //            System.out.println("---adding to pq " + child.number);
            }
        }
    }

    public int getMaxStart() {
        return maxStart;
    }

    public static void main(String[] args) {
        int limit = Integer.parseInt(args[0]);

        Collatz4 test = new Collatz4(limit);
        System.out.println(test.getMaxStart());
    }
}
