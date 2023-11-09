import java.io.IOException;
import java.util.Scanner;

public class Main {
       public static void main(String[] args) throws IOException {
              Scanner sc = new Scanner(System.in);

              int N, i, soma, quadrado, cubo;

              N = sc.nextInt();
              soma = 1;
              quadrado = 1;
              cubo = 1;

              for (i = 1; i <= N; i++) {
                     System.out.printf("%d %d %d%n", soma, quadrado, cubo);
                     soma += 1;
                     quadrado = soma * soma;
                     cubo = soma * soma * soma;
              }

              sc.close();
       }
}
