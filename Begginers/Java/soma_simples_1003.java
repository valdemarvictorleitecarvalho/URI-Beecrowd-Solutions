import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {

           Scanner sc = new Scanner(System.in);
           int A, B, SOMA;

           A = sc.nextInt();
           sc.nextLine();
           B = sc.nextInt();

           SOMA = A + B;

           System.out.printf("SOMA = %d%n", SOMA);
           
           sc.close();

    }
}
