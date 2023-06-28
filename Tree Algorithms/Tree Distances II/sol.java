
//TLE on 1 test case
import java.io.*;
import java.util.*;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static ArrayList<Integer>[] tree;
    public static int n;
    public static int[] subtree, distances;
    public static long[] allDistanceSum;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        n = cin.nextInt();
        tree = new ArrayList[n + 1];
        subtree = new int[n + 1];
        distances = new int[n + 1];
        allDistanceSum = new long[n + 1];

        for (int i = 0; i <= n; i++)
            tree[i] = new ArrayList<>();

        for (int i = 0; i < n - 1; i++) {
            int a = cin.nextInt();
            int b = cin.nextInt();
            tree[a].add(b);
            tree[b].add(a);
        }

        subtreeSize(1, 1);
        distanceFrom(1, 1, 0);

        long val = 0;
        for (int x : distances)
            val += x;

        allDistanceSum[1] = val + n;
        rerootingTree(1, 1);

        for (int i = 1; i <= n; i++)
            cout.print(allDistanceSum[i] + " ");

        cout.close();
    }

    public static void rerootingTree(int node, int parent) {
        allDistanceSum[node] = allDistanceSum[parent] + n - 2 * subtree[node];
        for (int child : tree[node])
            if (child != parent)
                rerootingTree(child, node);
    }

    public static int subtreeSize(int node, int parent) {
        for (int child : tree[node])
            if (child != parent)
                subtree[node] += subtreeSize(child, node);
        return ++subtree[node];
    }

    public static void distanceFrom(int node, int parent, int d) {
        distances[node] = d;
        for (int child : tree[node])
            if (child != parent)
                distanceFrom(child, node, d + 1);
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