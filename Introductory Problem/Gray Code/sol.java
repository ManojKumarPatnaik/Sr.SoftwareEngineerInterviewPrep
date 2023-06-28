import java.util.*;

public class sol {
    public static void main(String[] arg) {
        Scanner cin = new Scanner(System.in);
        int n = cin.nextInt();
        ArrayList<String> ans = gray(n);
        StringBuffer sb = new StringBuffer();
        for (String s : ans)
            sb.append(s + "\n");
        System.out.print(sb);
    }

    public static ArrayList<String> gray(int n) {
        if (n == 1)
            return new ArrayList<String>() {
                {
                    add("0");
                    add("1");
                }
            };
        ArrayList<String> sub = gray(n - 1);
        ArrayList<String> ans = new ArrayList<>();
        for (String s : sub)
            ans.add("0" + s);
        for (int i = sub.size() - 1; i >= 0; i--)
            ans.add("1" + sub.get(i));

        return ans;
    }
}