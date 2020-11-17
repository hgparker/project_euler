import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class MatrixNumberProducts {
    private int[] number;
    private long maxProduct;
    private int numberLength;
    private int productLength;

    public long getMaxProduct() {
        return maxProduct;
    }

    private void HandleInput(Scanner inputSource) {
        String num = inputSource.next();
        for (int k = 0; k < numberLength; k++)
            number[k] = num.charAt(k) - '0';
    }

    private void LookForProduct() {
        int startIndex = 0;
        int lastIndex = numberLength - productLength;
        long tempProduct = 1;
        boolean interrupted = true;

        while (startIndex <= lastIndex) {

            // Make new product, and if hit a zero, adjust startIndex, k, and make interrupted true
            if (interrupted) {
                tempProduct = 1;
                interrupted = false; // reset until we can guarantee we've been interrupted again

                for (int k = startIndex; k < startIndex + productLength; k++) {
                    tempProduct *= number[k];
                    if (number[k] == 0) {
                        startIndex = k;
                        k = startIndex + productLength;
                        interrupted = true;
                    }
                }
            } else {
                //since not interrupted we can just pay attention to beginning and start
                if (number[startIndex + productLength - 1] != 0) {
                    tempProduct /= number[startIndex - 1];
                    tempProduct *= number[startIndex + productLength - 1];
                } else {
                    tempProduct = 0;
                    startIndex = startIndex + productLength - 1;
                    interrupted = true;
                }
            }

            if (tempProduct > maxProduct)
                maxProduct = tempProduct;

            startIndex++;
        }
    }

    MatrixNumberProducts(Scanner inputSource, int nL, int nPL) {
        numberLength = nL;
        productLength = nPL;
        number = new int[numberLength];
        maxProduct = 0;

        HandleInput(inputSource);
        LookForProduct();
    }

    public static void main(String[] args) throws FileNotFoundException {
        File input = new File(args[0]);
        Scanner sc = new Scanner(input);
        int nL = Integer.parseInt(args[1]);
        int pL = Integer.parseInt(args[2]);

        MatrixNumberProducts calculator = new MatrixNumberProducts(sc, nL, pL);
        System.out.println(calculator.getMaxProduct());
    }
}
