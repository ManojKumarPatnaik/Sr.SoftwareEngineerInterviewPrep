import java.util.*;

public class sol{
    public static void main(String[] arg){
        Scanner cin = new Scanner(System.in);
        String s = cin.nextLine();
        long ans = 1;
        int i=0,j=0;

        while(i<s.length()){
            j = i+1;
            while(j<s.length() && s.charAt(i) == s.charAt(j))
                j++;
            ans = Math.max(ans,j-i);
            i = j;
        }
        System.out.println(ans);
    }
}