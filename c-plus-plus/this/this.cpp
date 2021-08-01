#include <iostream>
using namespace std;


class Hannah {
    public:
    	Hannah(int num) :h(num){
	}
	void printCrap(){
	    cout << "h = " << h << endl;
	    cout << "this->h = " << this->h << endl;
	    cout << "(*this).h = " << (*this).h << endl;
	}
    private:
        int h;
};

int main(){
    Hannah ho(23);
    ho.printCrap();    
}

