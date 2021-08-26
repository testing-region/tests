#include <iostream>
using namespace std;


template <class T>
class Pair {
	private:
		T first, second;
	public:
		Pair(T a, T b) : first(a), second(b) {}

		T bigger(){
		  return (first > second ? first : second);
		}
};

// template <class T>
// T Pair<T>::bigger() {
//	return (first > second ? first : second);
// }


int main() {
	Pair <int> obj(69, 245);
	cout << obj.bigger() << endl;
}
