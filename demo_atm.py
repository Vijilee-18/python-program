balance_amount =  1000
while True:
    print("\n1.\tcheck balance")
    print("2.\tDeposit money ")
    print("3.\tWithdraw money")
    print("4.\tExit")
    choice = int(input("enter your choice:"))
    if choice==1:
        print(f"The current balance ${balance_amount}")
    elif choice==2:
        deposit_amount = float(input("enter the amount:"))
        balance_amount=deposit_amount+balance_amount
        print(f"the deposit amount is {deposit_amount} and "
              f"balance amount is{balance_amount}")
    elif choice==3:
        withdraw_amount = float(input("enter the amount to withdraw:"))
        if withdraw_amount>balance_amount:
            print(f"Insufficient Balance")
        else:
            balance_amount=balance_amount-withdraw_amount
        print(f"The amount withdraw is{withdraw_amount}"
              f"Balance amount is:{balance_amount}")
    elif choice==4:
        break
    else:
        print("Invalid input:")