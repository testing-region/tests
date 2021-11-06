#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);

    // typedef is used to give a shorter name to a datatype
    // Sample:
    typedef long long ll;

    ll a = 123456789;
    ll b = 987654321;
    cout << a*b << '\n';

    // Macros
    // a macro means that certain strings in the code will be changed before compilation
    // they are defined using 'define' keyword
    // Sample:

    #define FIR(i,a,b) for (int i = a; i <= b; i++)
    
    FIR(i,1,10) {
        cout << i << '\n';
    }
}
