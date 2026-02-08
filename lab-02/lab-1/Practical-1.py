#Practical-01
print("Hello operations to Perform!:\n 1:income \n 2:Expense \n 3:Balance \n 4:exit")

def Summary():
    income = 0
    expense =0
    with open("Balance.txt","r") as file:
        for line in file:
            entry_type, amount = line.strip().split(":")
            amount = float(amount)

            if entry_type.strip() == "Income":
                income += amount
            elif entry_type.strip() == "Expense":
                expense += amount

    balance = income - expense
    print(f"Total Income: {income}")
    print(f"Total Expense: {expense}")
    print(f"Balance: {balance}")           

while True:
    o =int(input("Select operation (1/2/3/4):"))
    if o == 1:
        income =float(input("Enter Income Amount:"))
        with open("balance.txt","a") as file:
            file.write(f"Income:{income}\n")
        print(f"Income of {income} added.")

    elif o == 2:
        expense =float(input("Enter Expense Amount:"))
        with open("balance.txt","a") as file:
            file.write(f"Expense:{expense}\n")
        print(f"Expense of {expense} added.")
    
    elif o == 3:
        balance = income - expense
        with open("balance.txt","a") as file:
            file.write(f"Balance:{balance}\n")
        print(f"Blance of {balance} added.")    
    
    elif o == 4:
        print("Exit the program.")

        print("=============================================")
        c=open("balance.txt","r")
        data = c.read()
        print("Transaction History:\n",data)