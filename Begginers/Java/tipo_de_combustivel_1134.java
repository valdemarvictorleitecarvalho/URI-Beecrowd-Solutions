import java.io.IOException;
import java.util.Scanner;

public class Main {
       public static void main(String[] args) throws IOException {
              Scanner sc = new Scanner(System.in);

              int x, contador_gasolina, contador_alcool, contador_diesel;
              contador_gasolina = 0;
              contador_alcool = 0;
              contador_diesel = 0;

              while (true) {
                     x = sc.nextInt();

                     if (x == 4) {
                            break;
                     }
                     else if (x == 1) {
                            contador_alcool += 1;
                     }
                     else if (x == 2) {
                            contador_gasolina += 1;
                     }
                     else if (x == 3) {
                            contador_diesel += 1;
                     }
              }
              
              System.out.println("MUITO OBRIGADO");
              System.out.println("Alcool: " + contador_alcool);
              System.out.println("Gasolina: " + contador_gasolina);
              System.out.println("Diesel: " + contador_diesel);
              
              sc.close();

       }
}
