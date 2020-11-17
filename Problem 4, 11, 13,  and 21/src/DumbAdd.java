import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class DumbAdd {

    private int[] result;
    private int numDigits;

    public DumbAdd(int[][] addenda, int numAddenda, int addendumLength) {
        numDigits = 0;
        result = new int[addendumLength * 2];
        int intermediateSum = 0;
        int digit = 0;

        for (digit = 0; digit < addendumLength; digit++) {
            for (int p = 0; p < numAddenda; p++)
                intermediateSum += addenda[p][digit];

            result[digit] = intermediateSum % 10;
            intermediateSum /= 10;
        }

        while (intermediateSum > 0) {
            if (digit >= result.length)
                resultResize(result.length * 2);

            result[digit] = intermediateSum % 10;
            intermediateSum /= 10;
            digit++;
        }
        numDigits = digit;
    }

    private void resultResize(int newSize) {
        int[] newResult = new int[newSize];

        for (int k = 0; k < numDigits; k++)
            newResult[k] = result[k];

        for (int k = numDigits; k < newResult.length; k++)
            newResult[k] = 0;

        result = newResult;
    }

    public int[] getDigits(int digitsRequested) {
        if (digitsRequested > numDigits)
            throw new IllegalArgumentException("We ain't got that many digits!");
        int[] digits = new int[digitsRequested];
        for (int k = 1; k <= digitsRequested; k++)
            digits[digitsRequested - k] = result[numDigits - k];
        return digits;
    }

    public static void main(String[] args) {
        try {
            File file = new File("test.txt");
            Scanner scanner = new Scanner(file);

            int numAddenda = scanner.nextInt();
            int addendumLength = scanner.nextInt();
            int digitsDesired = scanner.nextInt();
            String str;

            int[][] addenda = new int[numAddenda][addendumLength];

            for (int p = 0; p < numAddenda; p++) {
                str = scanner.next();
                for (int k = 0; k < addendumLength; k++) {
                    addenda[p][k] = str.charAt(addendumLength - 1 - k) - '0';
                }
            }

            DumbAdd dumbAdd = new DumbAdd(addenda, numAddenda, addendumLength);

            int[] digits = dumbAdd.getDigits(digitsDesired);

            for (int k = digits.length - 1; k >= 0; k--)
                System.out.print(digits[k]);
            System.out.print("\n");

        } catch (FileNotFoundException e) {
            System.out.println("Where's the file, bro?");
        }
    }
}
