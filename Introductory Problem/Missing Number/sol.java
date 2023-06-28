import java.util.*;

public class sol {
    public static void main(String[] arg) {
        Scanner cin = new Scanner(System.in);
        long n = cin.nextLong();
        long sum = 0;
        for (int i = 0; i < n - 1; i++)
            sum += cin.nextLong();
        System.out.println(n * (n + 1) / 2 - sum);
    }
}