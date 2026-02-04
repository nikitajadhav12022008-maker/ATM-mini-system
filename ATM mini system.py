#ATM mini system:
balance = 10000
while True:
    print("1.Balance 2.Deposit 3.Withdraw 4.Exit")
    ch = int(input("choice:"))
    if(ch == 1):
        print(balance)
    elif(ch == 2):
        balance += int(input("enter amount:"))
        print("Amount deposited successfully!")
    elif(ch == 3):
        amt = int(input("enter amount:"))
        print("withdrawal successful!")
        if(amt <= balance):
            balance -= amt
        else:
            print("insufficient balance!")
    elif(ch == 4):
        print("Thank you for using ATM!")
        break
