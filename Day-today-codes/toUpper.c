#include<stdio.h>

void toUpper(char* c){
    *c = *c & ~32;
}

int main(){
    char c;
    scanf("%c", &c);
    toUpper(&c);
    printf("%c\n", c);
}