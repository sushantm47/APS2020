#include<stdio.h>

int main(){
  int t;
  scanf("%d", &t);
  while(t--){
    unsigned int a;
    scanf("%u", &a);
    printf("%u\n", ~a);
  }
}