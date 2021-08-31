#include <iostream>
#include <cmath>
using namespace std;


int main() {
    int a, b, c;
    double sqrtVal, x1, x2;

    cout << "Enter the value of a: ";
    cin >> a;
    cout << "Enter the value of b: ";
    cin >> b;
    cout << "Enter the value of c: ";
    cin >> c;

    sqrtVal = pow(b, 2) - (4*a*c);
    x1 = (-b + pow(sqrtVal, 0.5))/2*a;
    x2 = (-b - pow(sqrtVal, 0.5))/2*a;

    if(sqrtVal < 0) {
        cout << "No real roots!" << endl;
    } else {
        if(x1 == x2) {
	    cout << "The root of the equation is: " << x1 << endl;
	} else {
	    cout << "The roots of the equation are: " << x1 << " and " << x2 << endl;
	}
    }
}
