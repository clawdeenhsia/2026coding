//week03-3b.cpp
#include <stdio.h>
int main()
{
	int ans=0;
	for(int i=0;i<10;i++){
		int b;
		scanf("%d",&b);
		if(b%3==0) ans++;
	}
	printf("%d\n",ans);
}
