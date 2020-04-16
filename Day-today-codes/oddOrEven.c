#include<stdio.h>

//Will return 1 if odd
int isOdd(int n){
    return n&1;
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", isOdd(n));
}