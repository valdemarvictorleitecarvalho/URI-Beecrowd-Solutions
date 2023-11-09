import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
       public static void main(String[] args) throws IOException {
              Locale.setDefault(Locale.US);
              Scanner sc = new Scanner(System.in);

              int N, i;
              double X, Y, divisao;

              N = sc.nextInt();

              for (i = 0; i < N; i++) {
                     X = sc.nextDouble();
                     Y = sc.nextDouble();

                     if (Y == 0) {
                            System.out.println("divisao impossivel");
                     }
                     else {
                            divisao = X / Y;
                            System.out.printf("%.1f%n", divisao);
                     }
              }

              sc.close();

       }
}
