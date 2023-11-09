import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        double salario, valor;

        salario = sc.nextDouble();

        if (0.0 <= salario && salario <= 2000.0) {
            System.out.println("Isento");
        }
        else if (2000.0 < salario && salario <= 3000.0) {
            valor = (salario - 2000.0) * 0.08;
            System.out.printf("R$ %.2f%n", valor);
        }
        else if (3000 < salario && salario <= 4500) {
            valor = (salario - 3000) * 0.18 + (1000 * 0.08);
            System.out.printf("R$ %.2f%n", valor);
        }
        else if (salario > 4500) {
            valor = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08);
            System.out.printf("R$ %.2f%n", valor);
        }

        sc.close();

    }
}
