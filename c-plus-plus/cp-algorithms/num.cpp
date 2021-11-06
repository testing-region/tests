#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    // INTEGERS
    // int is of 32bit type (-2*10^9 ... 2*10^9)
    // long long is of 64bit type (-9*10^18 ... 9*10^18)
    // sample
    
    long long x = 123456789123456789LL;
    // the suffix 'LL' means it is of type long long
    cout << x << '\n';

    // note:
    int a = 123456789;
    long long b = a*a; 
    cout << b << '\n';    //wrong result
    // a is of type int so the result is also int
    // to get the correct result, do the ff:
    long long c = (long long) a*a;
    cout << c << '\n';

}
