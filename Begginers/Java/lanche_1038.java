import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int codigo, quantidade;
        double total;

        total = 0.0;
        codigo = sc.nextInt();
        quantidade = sc.nextInt();

        if (codigo == 1) {
            total = quantidade * 4.00;
        }
        else if (codigo == 2) {
            total = quantidade * 4.50;
        }
        else if (codigo == 3) {
            total = quantidade * 5.00;
        }
        else if (codigo == 4) {
            total = quantidade * 2.00;
        }
        else if (codigo == 5) {
            total = quantidade * 1.50;
        }

        sc.close();
        System.out.printf("Total: R$ %.2f%n", total);

    }
}
