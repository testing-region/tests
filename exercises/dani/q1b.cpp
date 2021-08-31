#include <iostream>
using namespace std;


int main() {
    int Hours, OvertimeHours;
    double Payrate, TotalPay, OvertimePay;
    cout << "Enter payrate: ";
    cin >> Payrate;
    cout << "Enter hours: ";
    cin >> Hours;

    if(Payrate < 10 and Hours > 40) {
        OvertimeHours = Hours - 40;
        OvertimePay = OvertimeHours * 1.5 * Payrate;
        TotalPay = 40 * Payrate + OvertimePay;
    } else {
        TotalPay = Hours * Payrate;
    }
}
