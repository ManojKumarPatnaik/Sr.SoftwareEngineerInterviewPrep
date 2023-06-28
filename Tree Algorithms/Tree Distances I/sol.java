//TLE on 3 test cases
import java.io.*;
import java.util.*;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static ArrayList<Integer>[] tree;
    public static int n;
    public static int[] ai, bi;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        n = cin.nextInt();
        tree = new ArrayList[n + 1];
        ai = new int[n + 1];
        bi = new int[n + 1];
        for (int i = 0; i <= n; i++)
            tree[i] = new ArrayList<>();
        for (int i = 0; i < n - 1; i++) {
            int a = cin.nextInt();
            int b = cin.nextInt();
            tree[a].add(b);
            tree[b].add(a);
        }

        int a = deepestNode(1, 1, height(1, 1));
        int b = deepestNode(a, a, height(a, a));

        distance(a, a, 0, ai);
        distance(b, b, 0, bi);

        for (int i = 1; i <= n; i++)
            cout.print(Math.max(ai[i], bi[i]) + " ");
        cout.close();
    }

    public static void distance(int node, int parent, int d, int[] arr) {
        arr[node] = d;
        for (int child : tree[node]) {
            if (child != parent) {
                distance(child, node, d + 1, arr);
            }
        }
    }

    public static int height(int node, int parent) {
        int h = -1;
        for (int child : tree[node]) {
            if (child != parent) {
                h = Math.max(h, height(child, node));
            }
        }
        return h + 1;
    }

    public static int deepestNode(int node, int parent, int h) {
        if (h == 0)
            return node;
        for (int child : tree[node]) {
            if (child != parent) {
                int res = deepestNode(child, node, h - 1);
                if (res != -1)
                    return res;
            }
        }
        return -1;
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