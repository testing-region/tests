// #include <iostream>
// #include <string>
// using namespace std;


// class TestClass{
//     public:
//         //Code written here can be used outside the class
//         void coolSay(){
//             cout << "Preaching to the choir" << endl;
//         }
// };

// class StringClass{
//     private:
//         string name;
    
//     public:
//         StringClass() {
//             cout << "This will be automatically called" ;
//         }

//         void setName(string x) {
//             name = x;
//         }

//         string getName() {
//             return name;
//         }
// };

// int main() {
//     //An object is used to access methods in a class
//     // TestClass testObject;
//     // testObject.coolSay();
//     StringClass test;
//     // test.setName("Tommy");
//     // cout << test.getName();
//     return 0;
// }

#include <iostream>
#include <string>
using namespace std;

class TestClass
{
public:
    TestClass(string z)
    {
        setName(z);
    }

    void setName(string x)
    {
        name = x;
    }

    string getName()
    {
        return name;
    }

private:
    string name;
};

int main()
{
    TestClass ob("Hello World");
    cout << ob.getName() << endl;
    TestClass ob1("Hello World");
    cout << ob1.getName();
    return 0;
}
