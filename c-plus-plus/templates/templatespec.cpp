#include <iostream>
using namespace std;


template <class T>
class MyClass {
	public:
		MyClass(T x) {
			cout << x << " is not a character" << endl;
		}
};


// using template specialisation
// testing for data type `char`
template <>
class MyClass <char> {
	public:
		MyClass(char x) {
			cout << x << " is a character" << endl;
		}
};


int main() {
    MyClass <int> obj1(7);
    MyClass <double> obj2(7.25);
    MyClass <char> obj3('d');
}
