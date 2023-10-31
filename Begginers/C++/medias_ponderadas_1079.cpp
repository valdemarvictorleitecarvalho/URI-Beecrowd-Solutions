#include <stdio.h>
 
int main() {
 
  int N, i;
  double X, Y, Z, media;
  
  scanf("%d", &N);
  
  for (int i = 1; i <= N; i++) {
      scanf("%lf %lf %lf", &X, &Y, &Z);
      media = ((X * 2) + (Y * 3) + (Z * 5)) / 10.0;
      printf("%.1lf\n", media);
      }
    return 0;
}
