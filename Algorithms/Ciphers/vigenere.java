
/**
 * Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic
 * substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple
 * substitution alphabets .The encryption of the original text is done using the Vigenère square or
 * Vigenère table.
 */

package ciphers;

public class vigenere  {

    public static String encrypt(final String message, final String key)
   {

       String result = "";

       for (int i = 0, j = 0; i < message.length(); i++) {
           char c = message.charAt(i);
           if (Character.isLetter(c)){
               if(Character.isUpperCase(c)) {
                   result += (char) ((c + key.toUpperCase().charAt(j) - 2 * 'A') % 26 + 'A');

               } else {
                   result += (char) ((c + key.toLowerCase().charAt(j) - 2 * 'a') % 26 + 'a');

               }
           } else {
               result+=c;
           }
           j = ++j % key.length();
       }
       return result;
   }

    public static String decrypt( final String message, final String key)
   {
       String result ="";

       for(int i = 0, j = 0; i < message.length(); i++){

           char c = message.charAt(i);
           if (Character.isLetter(c)){
               if(Character.isUpperCase(c)) {
                   result += ((char)('Z'-(25-(c-key.toUpperCase().charAt(j)))%26));

               } else {
                   result += ((char)('z'-(25-(c-key.toLowerCase().charAt(j)))%26));

               }
           } else {
               result+=c;
           }

           j = ++j % key.length();

       }
       return result;
    }
   public static void main (String [] args){
       String text="Hello World!";
       String key="itsakey";
       System.out.println(text);
       String ciphertext=encrypt(text, key);
       System.out.println(ciphertext);
       System.out.println(decrypt(ciphertext, key));

   }
}
