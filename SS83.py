class BankAccount:
    """A class to represent a bank account."""
    
    def __init__(self, account_number, holder_name, initial_balance=0):
        """Initialize bank account."""
        self.account_number = account_number
        self.holder_name = holder_name
        self._balance = initial_balance  # Protected attribute
        self._transaction_history = []  # Keep track of transactions
        self._log_transaction("Account opened", initial_balance)
    
    def deposit(self, amount):
        """Deposit money into account."""
        if amount <= 0:
            print("Deposit amount must be positive!")
            return False
        
        self._balance += amount
        self._log_transaction("Deposit", amount)
        return True
    
    def withdraw(self, amount):
        """Withdraw money from account."""
        if amount <= 0:
            print("Withdrawal amount must be positive!")
            return False
        
        if amount > self._balance:
            print("Insufficient funds!")
            return False
        
        self._balance -= amount
        self._log_transaction("Withdrawal", -amount)
        return True
    
    def get_balance(self):
        """Get current balance."""
        return self._balance
    
    def _log_transaction(self, transaction_type, amount):
        """Log a transaction."""
        self._transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'balance': self._balance
        })
    
    def display_statement(self):
        """Display account statement."""
        print("\nAccount Statement")
        print("-" * 50)
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Current Balance: ${self._balance:.2f}")
        
        print("\nTransaction History:")
        print("-" * 50)
        print("Type".ljust(15) + "Amount".ljust(15) + "Balance")
        print("-" * 50)
        for transaction in self._transaction_history:
            amount = transaction['amount']
            print(f"{transaction['type'].ljust(15)}${abs(amount):<14.2f}${transaction['balance']:.2f}")

def main():
    """Test the BankAccount class."""
    try:
        # Create account
        acc_num = input("Enter account number: ")
        name = input("Enter account holder name: ")
        initial_balance = float(input("Enter initial balance: $"))
        
        account = BankAccount(acc_num, name, initial_balance)
        
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Display Statement")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ")
            
            if choice == '1':
                amount = float(input("Enter deposit amount: $"))
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: $"))
                account.withdraw(amount)
            elif choice == '3':
                print(f"\nCurrent balance: ${account.get_balance():.2f}")
            elif choice == '4':
                account.display_statement()
            elif choice == '5':
                print("\nThank you for using our banking system!")
                break
            else:
                print("Invalid choice!")
                
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()
