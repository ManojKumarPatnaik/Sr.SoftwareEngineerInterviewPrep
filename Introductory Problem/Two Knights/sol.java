import java.util.*;

public class sol {
    public static void main(String[] arg) {
        Scanner cin = new Scanner(System.in);
        int n = cin.nextInt();
        for(long k=1;k<=n;k++){
            System.out.println(k*k*(k*k-1)/2 - 4*(k-1)*(k-2));
        }
    }
}