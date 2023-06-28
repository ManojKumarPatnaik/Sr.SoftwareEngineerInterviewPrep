import java.io.*;
import java.util.*;
import java.util.Map.Entry;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static int mod = (int) 1000000007;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        int a = cin.nextInt();
        int b = cin.nextInt();

        int[][] dp = new int[a + 1][b + 1];

        for (int i = 0; i <= a; i++)
            dp[i][1] = i - 1;
        for (int j = 0; j <= b; j++)
            dp[1][j] = j - 1;

        for (int i = 0; i <= a; i++) {
            for (int j = 0; j <= b; j++) {
                if (i == j)
                    dp[i][j] = 0;
                else {
                    dp[i][j] = i + j - 2;
                    for (int I = 1; I < i; I++)
                        dp[i][j] = Math.min(dp[i][j], dp[I][j] + dp[i - I][j] + 1);
                    for (int J = 1; J < j; J++)
                        dp[i][j] = Math.min(dp[i][j], dp[i][J] + dp[i][j - J] + 1);
                }
            }
        }
        cout.print(dp[a][b]);
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
