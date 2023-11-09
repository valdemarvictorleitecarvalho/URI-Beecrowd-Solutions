import java.io.IOException;
import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main(String[] args) throws IOException {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        int number, horas;
        double valor, salario;

        number = sc.nextInt();
        sc.nextLine();
        horas = sc.nextInt();
        sc.nextLine();
        valor = sc.nextDouble();

        salario = valor * horas;

        System.out.printf("NUMBER = %d%n", number);
        System.out.printf("SALARY = U$ %.2f%n", salario);
        
        sc.close();

    }
}
