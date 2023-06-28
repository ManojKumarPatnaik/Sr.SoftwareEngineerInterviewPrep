import java.util.*;

public class sol{
    public static void main(String[] arg){
        Scanner cin = new Scanner(System.in);
        int n = cin.nextInt();
        int[] arr = new int[n];
        for(int i=0;i<n;i++) arr[i] = cin.nextInt();

        HashSet<Integer> set = new HashSet<>();
        for(int i: arr)
            set.add(i);
        System.out.println(set.size());
    }
}