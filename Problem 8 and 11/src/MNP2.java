import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class MNP2 {

    private int[][] matrix;
    private long maxProduct;
    private int matrixDimension;
    private int productLength;

    public long getMaxProduct() {
        return maxProduct;
    }

    private void handleInput(Scanner inputSource) {

        for (int p = 0; p < matrixDimension; p++) {
            for (int k = 0; k < matrixDimension; k++) {
                matrix[p][k] = inputSource.nextInt();
            }
        }
    }

    private void test(int rowStart, int colStart, int rowDelta, int colDelta) {

        int rowFarthest = rowStart + (productLength - 1) * rowDelta;
        int colFarthest = colStart + (productLength - 1) * colDelta;

        if (rowFarthest < 0 || rowFarthest > (matrixDimension - 1))
            return;
        else if (colFarthest < 0 || colFarthest > (matrixDimension - 1))
            return;

        int p = rowStart;
        int k = colStart;
        long product = 1;

        while (p != (rowFarthest + rowDelta) || k != (colFarthest + colDelta)) {
            product *= matrix[p][k];
            p += rowDelta;
            k += colDelta;
        }

        if (product > maxProduct)
            maxProduct = product;
    }

    public MNP2(Scanner inputSource, int mD, int pL) {
        matrixDimension = mD;
        productLength = pL;
        matrix = new int[matrixDimension][matrixDimension];
        maxProduct = 0;

        handleInput(inputSource);

        for (int p = 0; p < matrixDimension; p++) {
            for (int k = 0; k < matrixDimension; k++) {
                test(p, k, 0, 1);
                test(p, k, 1, 0);
                test(p, k, 1, 1);
                test(p, k, -1, 1);
            }
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        File input = new File(args[0]);
        Scanner sc = new Scanner(input);

        MNP2 calculator = new MNP2(sc, 20, 4);
        System.out.println(calculator.getMaxProduct());
    }
}
