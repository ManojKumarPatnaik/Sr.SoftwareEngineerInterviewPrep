import java.io.* ;
import java.util.* ;
public class columnarcipher {

    // more information on
    //http://practicalcryptography.com/ciphers/columnar-transposition-cipher/
  //Decrypt operation 
  public static void decrypt(String s, String key) {
    int len = key.length();
    int len2 = s.length();
    String regex = "(?<=\\G.{" + Integer.toString(len2 / len) + "})";
    String arr[] = s.split(regex);
    HashMap < Character,
    String > hm = new HashMap < Character,
    String > ();
    char ch[] = key.toCharArray();
    Arrays.sort(ch);
    String key2 = new String(ch);
    String res = "";
    for (int i = 0; i < len; i++) {
      hm.put(key2.charAt(i), arr[i]);
    }
    for (int j = 0; j < len2 / len; j++) {
      for (int i = 0; i < len; i++) {
        res += hm.get(key.charAt(i)).charAt(j);
      }
    }
    System.out.println(res);
  }
  //Encrypt operation on string
  static public String encrypt(String s, String key) {
    int len = key.length();
    int len2 = s.length();
    int rem = len2 % len;
    String str = "";
    HashMap < Character,
    String > hm = new HashMap < Character,
    String > ();
    char ch[] = key.toCharArray();
    Arrays.sort(ch);
    String key2 = new String(ch);
    int start = 0,
    curr = 0;
    for (int i = 0; i < len; i++) {
      curr = start;
      str = "";
      while (curr < len2) {
        str += s.charAt(curr);
        curr += len;
      }
      start++;
      if (i >= rem) str += " ";
      hm.put(key.charAt(i), str);
    }
    String res = "";
    for (int i = 0; i < len; i++)
    res += (hm.get(key2.charAt(i)));
    return res;
  }
  //whitespace added as padding
  //runner class
  public static void main(String args[]) {
    InputStreamReader read = new InputStreamReader(System. in );
    BufferedReader in =new BufferedReader(read);
    String enc = encrypt("ParshwaShah", "CONSULT");
    System.out.println("Encrypted String: " + enc);
    System.out.print("Decrypted String: ");
    decrypt(enc, "CONSULT");

  }
}
