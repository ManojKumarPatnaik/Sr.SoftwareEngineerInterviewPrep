import java.util.*;

public class sol {
    public static void main(String[] arg) {
        Scanner cin = new Scanner(System.in);
        int n = cin.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = cin.nextInt();
        long ans = 0;
        for (int i = 1; i < n; i++) {
            if (arr[i] < arr[i - 1]) {
                ans += arr[i - 1] - arr[i];
                arr[i] = arr[i - 1];
            }
        }
        System.out.println(ans);
    }
}