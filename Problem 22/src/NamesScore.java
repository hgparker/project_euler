import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class NamesScore {

    private static int nameScore(String name) {
        int sum = 0;

        for (int k = 0; k < name.length(); k++)
            sum += name.charAt(k) - 'A' + 1;

        return sum;
    }

    public static void main(String[] args) throws FileNotFoundException {

        File namesFile = new File("p022_names.txt");
        Scanner sc = new Scanner(namesFile);
        sc.useDelimiter("[,\"]+");
        ArrayList<String> names = new ArrayList<>(5000);

        while (sc.hasNext())
            names.add(sc.next());

        names.sort(String::compareTo);

        int sum = 0;

        for (int k = 0; k < names.size(); k++)
            sum += (k + 1) * nameScore(names.get(k));

        System.out.println(sum);
        sc.close();
    }
}
