for i in range(5):
    Name = input("Enter Customer Name: ")
    Amount = int(input("Enter Purchase Amount: "))

    if Amount > 5000:
        Discount = 1000
    elif Amount > 2000:
        Discount = 500
    else:
        Discount = 0

    Final = Amount - Discount

    print("\nCustomer:", Name)
    print("Purchase Amount: ₹", Amount)
    print("Discount: ₹", Discount)
    print("Final Payable Amount: ₹", Final)
    print("-------------------")
