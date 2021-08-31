#include <iostream>
using namespace std;


int main() {
    double Cost, Revenue, Amount, Profit, Loss;
    cout << "Enter total cost: ";
    cin >> Cost;
    cout << "Enter total revenue: ";
    cin >> Revenue;
    Amount = Revenue - Cost;

    if(Amount > 0) {
       Profit = Amount;
       cout << "The profit is GHC " << Profit << endl;
    } else {
       Loss = abs(Amount);
       cout << "The loss is GHC " << Loss << endl;
    }
}

