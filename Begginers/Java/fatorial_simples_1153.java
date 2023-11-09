import java.io.IOException;
import java.util.Scanner;

public class Main {
       public static void main(String[] args) throws IOException {
              Scanner sc = new Scanner(System.in);

              int N, i;
              int fatorial = 1;

              N = sc.nextInt();

              for (i = 1; i <= N; i++) {
                     fatorial *= i;
              }

              System.out.println(fatorial);

              sc.close();
       }
}
