#include<stdio.h>

int getSetBits(int n){
    int count = 0;
    while(n){
        n = n & n-1;
        count++;
    }
    return(count);
}

int main(){
    int n;
    scanf("%d", &n);
    printf("%d", getSetBits(n));
}