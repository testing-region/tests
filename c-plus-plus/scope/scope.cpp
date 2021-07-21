#include <iostream>
using namespace std;

int tuna = 69;  	//all functions can use it

int main(){
	int tuna = 10; 	//only main can use it
	cout << tuna << endl;
	cout << ::tuna << endl;
}
