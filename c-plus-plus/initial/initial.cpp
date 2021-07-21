#include <iostream>
using namespace std;


int sum(int a, int b);

int main(){
	cout << sum(2, 8);
	return 0;
}

int sum(int a, int b) {
	return a + b;
}
