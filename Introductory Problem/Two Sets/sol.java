import java.util.*;

public class sol{
    public static void main(String[] arg){
        Scanner cin = new Scanner(System.in);
        long n = cin.nextLong();
        long sum = n*(n+1)/2;
        if(sum%2 == 1)
            System.out.println("NO");
        else{
            ArrayList<Long> a = new ArrayList<>();
            ArrayList<Long> b = new ArrayList<>();
            long bag = sum/2;
            for(long i=n;i>=1;i--){
                if(i<=bag){
                    a.add(i);
                    bag -= i;
                }
                else
                    b.add(i);
            }
            StringBuffer sb = new StringBuffer();
            sb.append("YES\n");
            sb.append(a.size()+"\n");
            for(long x:a)
                sb.append(x+" ");
            sb.append("\n");
            sb.append(b.size()+"\n");
            for(long x:b)
                sb.append(x+" ");
            System.out.println(sb);
        }
    }
}