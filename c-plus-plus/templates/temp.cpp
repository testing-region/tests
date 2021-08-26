#include <iostream>
using namespace std;

template <class T>
	T sum(T a, T b) {
	return a + b;
}

int main() {
	int x = 7, y = 3, z;
	z = sum(x, y);
	cout << z << endl;
}

