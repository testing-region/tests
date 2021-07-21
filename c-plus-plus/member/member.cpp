#include <iostream>
using namespace std;


class Body{
	public:
		Body(int a, int b) 
		: regVar(a), constVar(b)
		{	
		}
	
		void print() {
			cout << "The regular variable is: " << regVar << endl;
			cout << "The constant variable is: " << constVar << endl;
		}
	
	private:
		int regVar;
		const int constVar;
};

void testing(int var, int var1) {
	cout << var << " " << var1 << endl;
}

int main() {
	
	Body obj(5, 56);
	obj.print();

	testing(5, 24);
	
}
