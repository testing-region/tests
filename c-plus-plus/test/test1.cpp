#include <iostream>
using namespace std;


class Sally{
	public:
		Sally(){
		cout << "I am a constructor" << endl;
		}

		~Sally(){
		cout << "I am the deconstuctor" << endl;
		}

		void printCrap(){
			cout << "Did someone say steak?" << endl;
		}
};

int main(){
	Sally obj;
	cout << "Hellpo world!\n";
}
