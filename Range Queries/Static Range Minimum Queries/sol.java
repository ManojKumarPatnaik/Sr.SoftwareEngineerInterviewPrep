import java.io.*;
import java.util.*;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static long mod = (long) 1000000007;
    public static int INF = (int) 1e9;
    public static int n, q;
    public static int[] arr, st;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        n = cin.nextInt();
        q = cin.nextInt();
        int newN = nextPowerof2(n);
        arr = new int[newN];
        Arrays.fill(arr, INF);
        for (int i = 0; i < n; i++)
            arr[i] = cin.nextInt();
        n = newN;

        st = new int[2 * n];
        for (int i = 0; i < n; i++)
            update(i, arr[i]);

        while (q-- > 0) {
            int a = cin.nextInt();
            int b = cin.nextInt();
            cout.print(query(a, b, 1, n, 1) + "\n");
        }

        cout.close();
    }

    public static int query(int qa, int qb, int a, int b, int i) {
        if (qa <= a && b <= qb)
            return st[i];
        if (b < qa || a > qb)
            return INF;
        int mid = a + (b - a) / 2;
        return Math.min(query(qa, qb, a, mid, 2 * i), query(qa, qb, mid + 1, b, 2 * i + 1));
    }

    public static void update(int k, int x) {
        k += n;
        st[k] = x;
        k >>= 1;
        while (k >= 1) {
            st[k] = Math.min(st[2 * k], st[2 * k + 1]);
            k >>= 1;
        }
    }

    public static int nextPowerof2(int n) {
        if ((n & (n - 1)) == 0)
            return n;
        int p = 1;
        while (p < n)
            p = p << 1;
        return p;
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