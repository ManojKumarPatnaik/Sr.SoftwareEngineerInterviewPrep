import java.util.*;

public class sol {
    public static void main(String[] arg) {
        Scanner cin = new Scanner(System.in);
        int n = cin.nextInt();
        if(n==1)
            System.out.println(1);
        else if(n ==2 || n == 3)
            System.out.print("NO SOLUTION");
        else{
            StringBuffer sb = new StringBuffer();
            for(int i=2;i<=n;i+=2)
                sb.append(i+" ");
            for(int i=1;i<=n;i+=2)
                sb.append(i+" ");
            System.out.println(sb);
        }
        
    }
}
