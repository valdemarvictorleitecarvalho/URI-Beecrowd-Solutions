import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int codigo, numero_1, numero_2;
        double valor_1, pago_1,valor_2, pago_2, pago_total;

        codigo = sc.nextInt();
        numero_1 = sc.nextInt();
        valor_1 = sc.nextDouble();

        pago_1 = numero_1 * valor_1;

        sc.nextLine();
        codigo = sc.nextInt();
        numero_2 = sc.nextInt();
        valor_2 = sc.nextDouble();

        pago_2 = numero_2 * valor_2;

        pago_total = pago_1 + pago_2;

        System.out.printf("VALOR A PAGAR: R$ %.2f%n", pago_total);
        
        sc.close();

    }
}
