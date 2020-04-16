#include <stdio.h>
#include <x86intrin.h>
#include<limits.h>

int main(){
    printf("%lld",_popcnt64(ULLONG_MAX));
    return 0;
}