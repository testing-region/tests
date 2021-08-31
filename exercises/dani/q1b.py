Payrate = int(input("Enter payrate: "))
Hours = int(input("Enter hours: "))
if(Payrate < 10) and (Hours > 40):
    OvertimeHours = Hours - 40
    OvertimePay = OvertimeHours * 1.5 * Payrate
    TotalPay = 40 * Payrate + OvertimePay
else:
    TotalPay = Hours * Payrate
