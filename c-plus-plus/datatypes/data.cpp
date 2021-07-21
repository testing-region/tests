#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int intNum;
    long longNum;
    char charVal;
    float floatNum;
    double doubleNum;
    
    scanf("%d %ld %c %f %lf", &intNum, &longNum, &charVal, &floatNum, &doubleNum);
    printf("%d\n%ld\n%c\n%f\n%lf", intNum, longNum, charVal, floatNum, doubleNum);
    
    return 0;
}
