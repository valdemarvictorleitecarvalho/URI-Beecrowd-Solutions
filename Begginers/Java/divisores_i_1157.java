import java.io.IOException;
import java.util.Scanner;

public class Main {
       public static void main(String[] args) throws IOException {
              Scanner sc = new Scanner(System.in);

              int N, i;

              N = sc.nextInt();

              for (i = 1; i <= N; i++) {
                     if (N % i == 0) {
                            System.out.println(i);
                     }
              }

              sc.close();

       }
}
