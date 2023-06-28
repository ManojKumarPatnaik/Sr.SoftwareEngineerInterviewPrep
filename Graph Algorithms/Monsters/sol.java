//TLE on 3 test cases
import java.io.*;
import java.util.*;

public class sol {
    public static Reader cin;
    public static PrintWriter cout;
    public static long mod = (long) 1000000007;
    public static int n, m;
    public static HashMap<Character, Integer[]> track = new HashMap<>();
    public static HashMap<Character, Character> opposite = new HashMap<>();
    public static char[][] g;
    public static int[][] monsters;
    public static char[][] parent;

    public static void main(String[] arg) throws IOException {
        cin = new Reader(System.in);
        cout = new PrintWriter(new BufferedOutputStream(System.out));

        track.put('U', new Integer[] { -1, 0 });
        track.put('D', new Integer[] { 1, 0 });
        track.put('L', new Integer[] { 0, -1 });
        track.put('R', new Integer[] { 0, 1 });

        opposite.put('U', 'D');
        opposite.put('D', 'U');
        opposite.put('L', 'R');
        opposite.put('R', 'L');

        n = cin.nextInt();
        m = cin.nextInt();
        g = new char[n][m];
        monsters = new int[n][m];
        parent = new char[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(monsters[i], (int) 1e9);
            Arrays.fill(parent[i], 'X');
        }
        for (int i = 0; i < n; i++)
            g[i] = cin.next().toCharArray();

        bfs_monsters();
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if (g[i][j] == 'A') {
                    List<Object> res = bfs_player(i, j);
                    if ((boolean) res.get(0)) {
                        int a = (int) res.get(1);
                        int b = (int) res.get(2);
                        int cnt = 0;
                        StringBuffer sb = new StringBuffer();
                        while (a != i || b != j) {
                            sb.insert(0,opposite.get(parent[a][b]));
                            Integer[] t = track.get(parent[a][b]);
                            a = a + t[0];
                            b = b + t[1];
                            cnt++;
                        }
                        cout.print("YES\n");
                        cout.print(cnt + "\n");
                        cout.print(sb);
                    } else {
                        cout.print("NO");
                    }

                }
        cout.close();
    }

    public static boolean valid_block(int i, int j) {
        if (!(i >= 0 && i < n && j >= 0 && j < m))
            return false;
        return true;
    }

    public static boolean monsters_valid(int i, int j) {
        if (!(i >= 0 && i < n && j >= 0 && j < m))
            return false;
        if (monsters[i][j] != (int)1e9)
            return false;
        if (g[i][j] == '#')
            return false;
        return true;
    }

    public static boolean player_win(int i, int j, int level) {
        if (monsters[i][j] <= level)
            return false;
        if (i == 0 || i == n - 1 || j == 0 || j == m - 1)
            return true;
        return false;
    }

    public static boolean player_valid(int i, int j, int level) {
        if (!(i >= 0 && i < n && j >= 0 && j < m))
            return false;
        if (g[i][j] == '#')
            return false;
        if (monsters[i][j] <= level)
            return false;
        return true;
    }

    public static void bfs_monsters() {
        Queue<Integer[]> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (g[i][j] == 'M')
                    q.add(new Integer[] { i, j });
            }
        }
        int level = 0;
        while (q.size() > 0) {
            int length = q.size();
            for (int k = 0; k < length; k++) {
                Integer[] m = q.remove();
                int i = m[0];
                int j = m[1];
                if (!(monsters_valid(i, j)))
                    continue;
                monsters[i][j] = level;
                for (Map.Entry<Character, Integer[]> dir : track.entrySet()) {
                    int X = dir.getValue()[0];
                    int Y = dir.getValue()[1];
                    if (monsters_valid(i + X, j + Y))
                        q.add(new Integer[] { i + X, j + Y });
                }
            }
            level++;
        }
    }

    public static List<Object> bfs_player(int i, int j) {
        Queue<Integer[]> q = new LinkedList<>();
        q.add(new Integer[] { i, j });
        int level = 0;
        while (q.size() > 0) {
            int length = q.size();
            for (int k = 0; k < length; k++) {
                Integer[] m = q.remove();
                i = m[0];
                j = m[1];
                if (!(player_valid(i, j, level)))
                    continue;
                if (player_win(i, j, level))
                    return Arrays.asList(true, i, j);
                for (Map.Entry<Character, Integer[]> dir : track.entrySet()) {
                    int X = dir.getValue()[0];
                    int Y = dir.getValue()[1];
                    if (valid_block(i + X, j + Y)) {
                        q.add(new Integer[] { i + X, j + Y });
                        if (parent[i + X][j + Y] == 'X')
                            parent[i + X][j + Y] = opposite.get(dir.getKey());
                    }
                }
            }
            level++;
        }
        return Arrays.asList(false, -1, -1);
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