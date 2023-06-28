import java.util.*;

public class sol {

    public static StringBuffer sb = new StringBuffer();
    public static void main(String[] arg) {
        Scanner cin = new Scanner(System.in);
        int n = cin.nextInt();
        System.out.println((int)(Math.pow(2,n)-1));
        toh(n,1,3,2);
        System.out.print(sb);
    }

    public static void toh(int n,int source,int destination,int aux){
        if(n==1){
            sb.append(source+" "+destination+"\n");
            return;
        }
        toh(n-1,source,aux,destination);
        sb.append(source+" "+destination+"\n");
        toh(n-1,aux,destination,source);
    }
}