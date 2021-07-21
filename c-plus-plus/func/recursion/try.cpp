#include <iostream>
using namespace std;


int main(){
	int ans = 1;
	int x;
	cin >> x;

	for(int y = 1; y <= x; y++){
	    ans *= y;
	}

	cout << ans;
}
