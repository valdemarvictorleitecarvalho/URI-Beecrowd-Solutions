import java.io.IOException;
import java.util.Scanner;

public class Main {
       public static void main(String[] args) throws IOException {
              Scanner sc = new Scanner(System.in);

              int x;

              while (true) {
                     x = sc.nextInt();

                     if (x != 2002) {
                            System.out.println("Senha Invalida");
                     }
                     else {
                            System.out.println("Acesso Permitido");
                            break;
                     }
              }

              sc.close();

       }
}
