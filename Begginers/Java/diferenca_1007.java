import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int A, B, C, D, diferenca;

        A = sc.nextInt();
        sc.nextLine();
        B = sc.nextInt();
        sc.nextLine();
        C = sc.nextInt();
        sc.nextLine();
        D = sc.nextInt();

        diferenca = ((A * B) - (C * D));

        System.out.printf("DIFERENCA = %d%n", diferenca);
        
        sc.close();

    }
}
