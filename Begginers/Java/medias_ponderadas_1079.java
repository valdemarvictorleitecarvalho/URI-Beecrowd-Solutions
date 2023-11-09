import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

public class Main {
       public static void main(String[] args) throws IOException {
              Locale.setDefault(Locale.US);
              Scanner sc = new Scanner(System.in);

              int N, i;
              double A, B, C, media;

              N = sc.nextInt();

              for (i = 0; i < N; i++) {
                     A = sc.nextDouble();
                     B = sc.nextDouble();
                     C = sc.nextDouble();

                     media = ((A * 2) + (B * 3) + (C * 5)) / 10;

                     System.out.printf("%.1f%n", media);
              }

              sc.close();

       }
}
