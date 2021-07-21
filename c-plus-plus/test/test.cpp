#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;


int main(){
	srand(time(0));    //allows to alter the rand algorithm to make the numbers truly random
	for(int x = 1; x < 25; x++){ 
		cout << 1 + (rand() % 6) << endl;
	}
}
