//week03-4.cpp
#include <stdio.h>
int main()
{
	int N;
	scanf("%d",&N);
	int ans=0;
	for(int i=1;i<=N;i++){
		if(N%i==0) ans++;
	}
	printf("%d\n",ans);
}
