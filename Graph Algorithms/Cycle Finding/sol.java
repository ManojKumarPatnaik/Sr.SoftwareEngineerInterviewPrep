
import java.io.*;
import java.util.*;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static long mod = (long) 1000000007;
    public static long INF = (long) 1e18;
    public static int n, m, lastRelaxed;
    public static int[] u, v, c, parent;
    public static long[] d;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        n = cin.nextInt();
        m = cin.nextInt() + n;

        // storing only edges
        u = new int[m];
        v = new int[m];
        c = new int[m];
        d = new long[n + 1];
        parent = new int[n + 1]; // for tracing back

        Arrays.fill(d, INF);
        for (int i = 0; i < m - n; i++) {
            u[i] = cin.nextInt();
            v[i] = cin.nextInt();
            c[i] = cin.nextInt();
        }
        for (int i = 1; i <= n; i++) { // adding dummy node
            u[i + m - n - 1] = 0;
            v[i + m - n - 1] = i;
            c[i + m - n - 1] = 0;
        }

        d[0] = 0; // dummy node as source

        for (int i = 0; i < n; i++) 
            relax();

        if (relax()) {

            for (int i = 0; i < n; i++)// for entering the cycle
                lastRelaxed = parent[lastRelaxed];

            StringBuffer sb = new StringBuffer();
            int temp = lastRelaxed;
            sb.insert(0, temp + " ");
            temp = parent[lastRelaxed];
            while (temp != lastRelaxed) {
                sb.insert(0, temp + " ");
                temp = parent[temp];
            }
            sb.insert(0, temp + " ");

            cout.print("YES\n");
            cout.print(sb);
        } else {
            cout.print("NO");
        }

        cout.close();
    }

    public static boolean relax() {
        boolean res = false;
        for (int i = 0; i < m; i++) {
            long newd = d[u[i]] + c[i];
            if (newd < d[v[i]]) {
                d[v[i]] = newd;
                lastRelaxed = v[i];
                parent[v[i]] = u[i];
                res = true;
            }
        }

        return res;
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