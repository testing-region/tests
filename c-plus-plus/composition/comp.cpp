#include <iostream>
#include <string>
using namespace std;



class Birthday {
	public:
		Birthday(int d, int m, int y)
		: month(m), day(d), year(y)
		{
		}

		void printDate() {
			cout << day << "/"  << month << "/" << year << endl;
		}
	private:
		int month;
		int day;
		int year;
};

class People {
	public:
		People(string x, Birthday bo)
		: name(x), dateOfBirth(bo)
		{
		}

		void printInfo() {
			cout << name << " was born on ";
			dateOfBirth.printDate();
		}
	private:
		string name;
		Birthday dateOfBirth;
};

int main() {
	Birthday birthObj(20, 30, 2002);
	People person("David", birthObj);
	person.printInfo();
}

