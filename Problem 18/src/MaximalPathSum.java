import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class MaximalPathSum {
    private int maximalPath;

    public int getMaximalPath() {
        return maximalPath;
    }

    public MaximalPathSum(int numRows, int weights[][]) {
        int[][] paths = new int[numRows][numRows];

        //Initialize left & right slopes
        paths[0][0] = weights[0][0];
        for (int k = 1; k < numRows; k++) {
            paths[k][0] = paths[k - 1][0] + weights[k][0];
            paths[k][k] = paths[k - 1][k - 1] + weights[k][k];
        }

        //Calculating intermediate values
        for (int k = 1; k < numRows; k++) {
            for (int p = 1; p < k; p++) {
                if (paths[k - 1][p - 1] < paths[k - 1][p])
                    paths[k][p] = paths[k - 1][p];
                else
                    paths[k][p] = paths[k - 1][p - 1];
                paths[k][p] += weights[k][p];
            }
        }

        //Get max from final row
        maximalPath = paths[numRows - 1][0];

        for (int k = 1; k < numRows; k++)
            if (paths[numRows - 1][k] > maximalPath)
                maximalPath = paths[numRows - 1][k];
    }

    public static void main(String[] args) {
        try {
            File file = new File(args[0]);
            Scanner scanner = new Scanner(file);
            int numRows = scanner.nextInt();
            int[][] data = new int[numRows][numRows];

            //Input data
            for (int k = 0; k < numRows; k++) {
                for (int p = 0; p <= k; p++) {
                    data[k][p] = scanner.nextInt();
                }
            }
            MaximalPathSum mps = new MaximalPathSum(numRows, data);
            System.out.println(mps.getMaximalPath());
        } catch (FileNotFoundException e) {
            System.out.println("Where's the file, brah?");
        }
    }

}
