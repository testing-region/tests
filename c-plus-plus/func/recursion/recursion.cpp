#include <iostream>
using namespace std;


int factorial(int x){
    if(x == 1 || x == 0){
       return 1;
    } else{
        return x * factorial(x-1);
    }
}


int fact(int x){
    int ans = 1;

    if(x == 1 || x == 0){
       return 1;
    }
    
     for(int y = 1; y <= x; y++){
           ans *= y;
        }
     return ans;
}

int main()
{
    int a;
    cin >> a;
    cout << factorial(a);
}
