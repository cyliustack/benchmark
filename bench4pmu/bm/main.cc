#include<iostream>
#include<stdio.h>
#include<cstdlib>

using namespace std;


int main(int argc, char* argv[]){
    
    if( argc < 3 ){
        printf("usage: ./a.out N way\n");
        exit(0);
    }
    int N = atoi(argv[1]);
    int way = atoi(argv[2]);
    printf("num of loops = %d\n", N);
    printf("num of ways = %d\n", way);
    long int res=0;
    for(int i=0; i<N ;i++){
        if(lrand48()%way ==0)
           res += i*i*i*i;
    }
    printf("res = %ld\n", res);
    return 0;
}
