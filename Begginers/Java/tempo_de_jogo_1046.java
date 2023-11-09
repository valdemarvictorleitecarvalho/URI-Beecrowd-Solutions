import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int hora_1, hora_2, total;

        hora_1 = sc.nextInt();
        hora_2 = sc.nextInt();

        if (hora_1 == hora_2) {
            System.out.println("O JOGO DUROU 24 HORA(S)");
        }
        else if (hora_1 > hora_2) {
            total = (24 - hora_1) + hora_2;
            System.out.printf("O JOGO DUROU %d HORA(S)%n", total);
        }
        else {
            total = Math.abs(hora_2 - hora_1);
            System.out.printf("O JOGO DUROU %d HORA(S)%n", total);
        }
        
        sc.close();

    }
}
