#include <iostream>
using namespace std;


class Stank{
	public:
		Stank(){
			stinky = 0;
		}
	private:
		int stinky;
	
	friend void stanksFriend(Stank &sfo);
};

void stanksFriend(Stank &sfo){
	sfo.stinky = 99;
	cout << sfo.stinky << endl;
}


int main(){
	Stank bob;
	stanksFriend(bob);
}
