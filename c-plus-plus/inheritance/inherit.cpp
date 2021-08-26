#include <iostream>
using namespace std;

class Mother {
	public:
		void sayName() {
			cout << "I am a Saah" << endl;
		}
};

class Daughter : public Mother {
	public:

};

int main () {
	Mother mom;
	mom.sayName();

	Daughter tina;
	tina.sayName();
}
