#include <stdio.h>

// https://www.hackerrank.com/challenges/a-very-big-sum?h_r=next-challenge&h_v=zen

int main(){
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
    }

    long long int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    printf("%lld", sum);

    return 0;
}
