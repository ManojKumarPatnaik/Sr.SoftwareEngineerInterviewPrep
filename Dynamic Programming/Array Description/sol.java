import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static long[] memo;
    public static int mod = (int)1000000007;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        int n = cin.nextInt();
        int m = cin.nextInt();
        int[] x =new int[n];
        int[][] dp = new int[n+1][m+1];

        for(int i=0;i<n;i++) x[i] = cin.nextInt();
        Arrays.fill(dp[n],1);
        dp[n][0] = 0;

        for(int i=n-1;i>=0;i--){
            for(int j=1;j<=m;j++){
                if(x[i] == 0){
                    for(int k=j-1;k<=j+1;k++)
                        if(k<=m)
                            dp[i][j] = (dp[i][j]+dp[i+1][k])%mod;
                }
                else if(Math.abs(x[i]-j)<=1)
                    dp[i][j] = dp[i+1][x[i]];
                else
                    dp[i][j] = 0;
            }
        }

        if(x[0] == 0){
            int ans = 0;
            for(int i=1;i<=m;i++)
                ans = (ans+dp[1][i])%mod;
            cout.print(ans%mod);
        }
        else    
            cout.print(dp[1][x[0]]);
        cout.close();
    }

    static class Reader {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader(InputStream is) {
            din = new DataInputStream(is);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public Reader(String file_name) throws IOException {
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public String nextLine() throws IOException {
            byte[] buf = new byte[1000000]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == '\n')
                    break;
                buf[cnt++] = (byte) c;
            }
            return new String(buf, 0, cnt);
        }

        public String next() throws IOException {
            byte[] buf = new byte[1000000]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1) {
                if (c == ' ' || c == '\n' || c == '\t')
                    break;
                buf[cnt++] = (byte) c;
            }
            return new String(buf, 0, cnt);
        }

        public int nextInt() throws IOException {
            int ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (neg)
                return -ret;
            return ret;
        }

        public long nextLong() throws IOException {
            long ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
            return ret;
        }

        public double nextDouble() throws IOException {
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();

            do {
                ret = ret * 10 + c - '0';
            } while ((c = read()) >= '0' && c <= '9');

            if (c == '.') {
                while ((c = read()) >= '0' && c <= '9') {
                    ret += (c - '0') / (div *= 10);
                }
            }

            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }

        public void close() throws IOException {
            if (din == null)
                return;
            din.close();
        }
    }
}
