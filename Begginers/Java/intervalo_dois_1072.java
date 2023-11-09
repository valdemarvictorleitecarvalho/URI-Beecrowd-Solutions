import java.io.IOException;
import java.util.Scanner;

public class Main {
       public static void main(String[] args) throws IOException {
              Scanner sc = new Scanner(System.in);

              int N, X, i, in, out;

              N = sc.nextInt();
              in = 0;
              out = 0;

              for (i = 0; i < N; i++) {
                     X = sc.nextInt();

                     if (X >= 10 && X <= 20) {
                            in += 1;
                     }
                     else {
                            out += 1;
                     }
              }

              sc.close();
              System.out.println(in + " in");
              System.out.println(out + " out");

       }
}
