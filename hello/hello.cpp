#include <iostream>

int fact(int x){
    if (x == 1){
	return 1;
    } else {
	return x * fact(x-1);
    }
}

int main(){
    std::cout << fact(20) << std::endl;
}
