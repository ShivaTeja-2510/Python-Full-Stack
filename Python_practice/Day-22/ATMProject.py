pin="1234"
balance=50000
attempts=0
maxAttempts=3
transac=[]
while True:
    enterpin=input("Enter your pin: ")
    if pin==enterpin:
        print("Pin verification is successful")
        break
    else:
        attempts+=1
        print("Pin is invalid, remaining attempts are:",(maxAttempts-attempts))
        if attempts>=maxAttempts:
            print("Card is blocked due to limit exceeded...")
            exit()
print("next you will see menu...")
# Main Functionality
while True:
    print("---------Your Menu----------")
    print("press-1 for checking the balance")
    print("press-2 for deposit")
    print("press-3 for withdrawl")
    print("press-4 to see the last 4 transactions")
    print("press-5 to exit")
    choice = int(input("Enter your choice: "))
    if choice==1:
        print("Your Total Balance is:",balance)
    elif choice==2:
        amount = int(input("Enter amount to deposit: "))
        if amount>0:
            balance+=amount
            transac.append(f"Deposited amount is: {amount}")
            if len(transac)>5:
                transac.pop(0)
            print("Amount is Deposited, Current balance is:",balance)
        else:
            print("Please enter a valid amount")
    elif choice==3:
        amount = int(input("Enter amount to withdraw: "))
        if amount>0 and amount<=balance:
            balance-=amount
            transac.append(f"Withdrawn amount is: {amount}")
            if len(transac)>5:
                transac.pop(0)
            print("Amount is Withdrawn, Current balance is:",balance)
        else:
            print("Please enter a valid amount or insufficient balance")
    elif choice==4:
        if len(transac)!=0:
            for t in transac:
                print(t)
        else:
            print("No Transactions Happened")
    elif choice==5:
        break
    else:
        print("Invalid Choice, Please give the Correct Choice: ")
print("End of The Project....")
