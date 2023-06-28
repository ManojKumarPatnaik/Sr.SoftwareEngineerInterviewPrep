import java.util.*;

public class sol{
    public static void main(String[] arg){
        Scanner cin = new Scanner(System.in);
        long n = cin.nextLong();
        while(n!=1){
            System.out.print(n+" ");
            n = (n%2==0)?n/2:3*n+1;
        }
        System.out.println(1);
    }
}