#include <iostream>
using namespace std;


void passByValue(int x);
void passByReference(int *x);

int main(){
	int apple = 13;
	int orange = 13;
	
	passByValue(apple);
	passByReference(&orange);

	cout << apple << endl;
	cout << orange << endl;
}

void passByValue(int x){
	x = 99;
}

void passByReference(int *x){
	*x = 66;
}
