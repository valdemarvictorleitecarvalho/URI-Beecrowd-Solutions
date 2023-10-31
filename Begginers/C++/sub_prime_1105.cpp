#include <stdio.h>
 
int main() {
 
int b, n;
	
	int fundo[30]; 
	
	while(true){ 
		
		scanf("%d %d", &b, &n); 
		
		if(b==0 && n==0) break; 
		
		for(int i=1; i<=b; i++) scanf("%d", &fundo[i]); 
		
		for(int i=1; i<=n; i++){ 
			
			int d, c, v; 
			scanf("%d %d %d", &d, &c, &v); 
			
			fundo[d]-=v; 
			fundo[c]+=v; 
		}
		
		int ajuda=0; 
		for(int i=1; i<=b; i++) if(fundo[i]<0) ajuda=1;
		
		if(ajuda==0) printf("S\n"); 
		else printf("N\n"); 
	}
	 
	return 0;
}
