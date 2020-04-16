#include<stdio.h>

void toLower(char* c){
    *c = *c | 32;
}

int main(){
    char c;
    scanf("%c", &c);
    toLower(&c);
    printf("%c\n", c);
}