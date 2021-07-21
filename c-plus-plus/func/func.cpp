#include <iostream>
using namespace std;

//function overloading


void printNumber(int x){
    cout << "I am printing an integer " << x << endl;
}

void printNumber(float y){
    cout << "I am printing a float " << y << endl;
}

int main()
{
    int a = 54;
    float b = 32.4896;

    printNumber(a);
    printNumber(b);
}
