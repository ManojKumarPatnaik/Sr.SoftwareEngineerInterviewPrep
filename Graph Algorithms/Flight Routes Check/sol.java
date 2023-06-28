
import java.io.*;
import java.util.*;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static long mod = (long) 1000000007;
    public static int n, m;
    public static ArrayList<Integer>[] g;
    public static ArrayList<Integer>[] grev;
    public static boolean[] visited;
    public static Stack<Integer> stack;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        n = cin.nextInt();
        m = cin.nextInt();

        g = new ArrayList[n + 1];
        grev = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            g[i] = new ArrayList<Integer>();
            grev[i] = new ArrayList<Integer>();
        }
        visited = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            int a = cin.nextInt();
            int b = cin.nextInt();
            g[a].add(b);
            grev[b].add(a);
        }

        stack = new Stack<>();
        for (int i = 1; i <= n; i++)
            if (!visited[i])
                dfs1(g, i);

        Arrays.fill(visited, false);
        dfs2(grev, stack.peek());
        int cnt = 0;
        for (int i = 1; i <= n; i++)
            if (visited[i])
                cnt++;

        if (cnt == n) {
            cout.print("YES");
        } else {
            int f = 0;
            for (int i = 1; i <= n; i++)
                if (!visited[i]) {
                    f = i;
                    break;
                }
            int t = 0;
            for (int i = 1; i <= n; i++)
                if (visited[i]) {
                    t = i;
                    break;
                }
            cout.print("NO\n");
            cout.print(f + " " + t);
        }

        cout.close();
    }

    public static void dfs1(ArrayList<Integer>[] graph, int node) {
        visited[node] = true;
        for (int child : graph[node]) {
            if (!visited[child])
                dfs1(graph, child);
        }
        stack.push(node);
    }

    public static void dfs2(ArrayList<Integer>[] graph, int node) {
        visited[node] = true;
        for (int child : graph[node]) {
            if (!visited[child])
                dfs2(graph, child);
        }
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