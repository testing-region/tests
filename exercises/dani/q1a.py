Cost = float(input("Enter total cost: "))
Revenue = float(input("Enter total revenue: "))
Amount = Revenue - Cost
if Amount > 0:
    Profit = Amount
    print("The profit is GHC " + str(Profit))
else:
    Loss = abs(Amount)
    print("The loss is GHC " + str(Loss))
