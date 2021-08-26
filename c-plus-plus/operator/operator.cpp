#include <iostream>
using namespace std;

class Sally {
    public:
	int num;
	Sally() {
	}
	Sally(int a) {
		num = a;
	}
	Sally operator+(Sally aso) {
		Sally brandNew;
		brandNew.num = num + aso.num;
		return (brandNew);
	}
};


int main() {
	Sally a(34);
	Sally b(21);
	Sally c;

	c = a;
	cout << c.num << endl;
	c = a + b;
	cout << c.num;
}
