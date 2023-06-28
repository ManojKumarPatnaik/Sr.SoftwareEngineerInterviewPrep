import java.util.*;

public class sol {
    public static void main(String[] arg) {
        Scanner cin = new Scanner(System.in);
        long t = cin.nextLong();
        StringBuffer sb = new StringBuffer();
        while(t-- >0){
            long x = cin.nextLong();
            long y = cin.nextLong();
            long sq = Math.max(x,y);
            if(sq%2 == 0)   
                sb.append((sq-1)*(sq-1) + x + (sq-y)+"\n");
            else
                sb.append(sq*sq - x - (sq-y) + 1+"\n");
        }
        System.out.println(sb);
    }
}