import java.io.*;
import java.util.*;

public class sol {
    public static void main(String[] arg) throws IOException, NumberFormatException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        int[] b = new int[m];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            a[i] = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++)
            b[i] = Integer.parseInt(st.nextToken());

        shuffleArray(a);
        shuffleArray(b);
        Arrays.sort(a);
        Arrays.sort(b);

        int ans = 0;
        int x = 0, y = 0;
        while (x < n && y < m) {
            if (Math.abs(a[x] - b[y]) <= k) {
                x++;
                y++;
                ans++;
            } else if (a[x] + k < b[y])
                x++;
            else
                y++;
        }

        System.out.println(ans);
    }

    public static void shuffleArray(int[] arr) {
        int n = arr.length;
        Random rnd = new Random();
        for (int i = 0; i < n; ++i) {
            int tmp = arr[i];
            int randomPos = i + rnd.nextInt(n - i);
            arr[i] = arr[randomPos];
            arr[randomPos] = tmp;
        }
    }
}