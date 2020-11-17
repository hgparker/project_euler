import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SmartAdd {

    public static void main(String[] args) {
        try {
            File file = new File("test.txt");
            Scanner scanner = new Scanner(file);

            int numAddenda = scanner.nextInt();
            int addendumLength = scanner.nextInt();
            int digitsDesired = scanner.nextInt();
            String str;

            int inputLength = Math.min(digitsDesired + 2, addendumLength);

            int[][] addenda = new int[numAddenda][inputLength];

            for (int p = 0; p < numAddenda; p++) {
                str = scanner.next();
                for (int k = 0; k < inputLength; k++) {
                    addenda[p][k] = str.charAt(inputLength - 1 - k) - '0';
                }
            }

            DumbAdd dumbAdd = new DumbAdd(addenda, numAddenda, inputLength);

            int[] digits = dumbAdd.getDigits(digitsDesired);

            for (int k = digits.length - 1; k >= 0; k--)
                System.out.print(digits[k]);
            System.out.print("\n");

        } catch (FileNotFoundException e) {
            System.out.println("Where's the file, bro?");
        }
    }
}
