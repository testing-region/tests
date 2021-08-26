#include <iostream>
using namespace std;

template <class T, class U>
U smaller(T a, U b) {
    return (a < b ? a : b);
}

int main(){
    cout << smaller(1, 4.25) << endl;
}
