#include <iostream>
#include <cmath>
using namespace std;


int main(){

	float amount, principal = 10000, rate = 0.03;
	
	for(int day = 0; day <= 20; day++){
		amount = principal * pow(1+rate, day);
		cout << day << "--------" << amount << endl;
	}
}
