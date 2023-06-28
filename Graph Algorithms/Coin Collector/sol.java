import java.io.*;
import java.util.*;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static long mod = (long) 1000000007;
    public static int n, m;
    public static ArrayList<Integer>[] g;
    public static ArrayList<Integer>[] grev;
    public static ArrayList<Integer>[] dag;
    public static long[] ssrCost;
    public static int[] nodeCost;
    public static boolean[] visited;
    public static Stack<Integer> stack;
    public static int[] label;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        n = cin.nextInt();
        m = cin.nextInt();
        nodeCost = new int[n + 1];
        label = new int[n + 1];
        g = new ArrayList[n + 1];
        grev = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            g[i] = new ArrayList<Integer>();
            grev[i] = new ArrayList<Integer>();
        }

        for (int i = 1; i <= n; i++)
            nodeCost[i] = cin.nextInt();

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
        int l = 1;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            if (!visited[node])
                dfs2(grev, node, l++);
        }

        int newN = l - 1;
        ssrCost = new long[newN + 1];
        for (int i = 1; i <= n; i++)
            ssrCost[label[i]] += nodeCost[i];

        dag = new ArrayList[newN + 1];
        for (int i = 0; i <= newN; i++)
            dag[i] = new ArrayList<Integer>();
        for (int i = 1; i <= n; i++) {
            for (int j : g[i]) {
                if (label[i] != label[j]) {
                    dag[label[i]].add(label[j]);
                }
            }
        }
        Arrays.fill(visited, false);
        for (int i = 1; i <= newN; i++)
            if (!visited[i])
                dfs3(dag, i);
        long ans = 0;
        for (int i = 1; i <= newN; i++)
            ans = Math.max(ans, ssrCost[i]);
        cout.print(ans);
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

    public static void dfs2(ArrayList<Integer>[] graph, int node, int l) {
        visited[node] = true;
        label[node] = l;
        for (int child : graph[node]) {
            if (!visited[child])
                dfs2(graph, child, l);
        }
    }

    public static long dfs3(ArrayList<Integer>[] graph, int node) {
        if (visited[node])
            return ssrCost[node];
        long max = 0;
        for (int child : graph[node]) {
            if (!visited[child])
                dfs3(graph, child);
            max = Math.max(max, ssrCost[child]);
        }
        ssrCost[node] += max;
        visited[node] = true;
        return ssrCost[node];
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