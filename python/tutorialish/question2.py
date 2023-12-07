def sum_of_products(list1, list2):
    product_sum = 0

    for item1, item2 in zip(list1, list2):
        product_sum = product_sum + (item1 * item2)

    return product_sum


# print(sum_of_products([2, 4, 6], [1.5, 2.0, 6.5]))


quantity = [5, 2, 8, 14]
unit_prices = [1.5, 2.0, 3.5, 0.2]

print("Total price is GHC", sum_of_products(quantity, unit_prices))
