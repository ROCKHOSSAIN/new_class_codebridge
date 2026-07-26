current_balance = 100000
deposit_count = 0;
withdraw_count = 0;
transactions_amounts = []
balance_history=[]
transaction_type = []

while True:
    transaction_type_input = input("Enter transaction type (deposit/withdraw or 'done'): ")
    if(transaction_type_input.upper()=="DEPOSIT"):
        deposit_amount = int (input("Enter transaction amount: "))
        current_balance += deposit_amount
        deposit_count += 1
        balance_history.append(current_balance)
        transactions_amounts.append(+deposit_amount)
        transaction_type.append("DEPOSIT")
        # print((f"current am:{current_balance}"))
    if(transaction_type_input.upper()=="WITHDRAW"):
        withdraw_amount = int (input("Enter transaction amount: "))
       
        if(withdraw_amount<= current_balance):
            transactions_amounts.append(-withdraw_amount)
            current_balance -= withdraw_amount
            withdraw_count += 1
            balance_history.append(current_balance)
            transaction_type.append("WITHDRAW")
        else:
            print("Insufficient balance for withdrawal.")
            # print(current_balance)
        

    if(transaction_type_input.upper()=="DONE"):
        break
print("--------------------------------------------")
print("TRANSACTION HISTORY");
print("--------------------------------------------")
print("No. | Type | Amount | Balance")

i=0;
while i<len(transaction_type):
   print(f"{i+1} | {transaction_type[i]} | {transactions_amounts[i]} | {balance_history[i]}")

   i=i+1;

print("--------------------------------------------")
print(f"Total Deposits: {deposit_count}")
print(f"Total Withdrawals: {withdraw_count}")
print(f"Closing  Balance: {balance_history[-1]}")