class SavingsAccount:
    
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
        
        if initial_balance > 0:
            self.transactions.append(f"INITIAL DEPOSIT: +${initial_balance} - Balance: ${initial_balance}")
    
    def deposit(self, amount):
        if amount <= 0:
            return {"success": False, "message": "❌ Amount must be positive"}
        self.balance += amount
        self.transactions.append(f"DEPOSIT: +${amount} - Balance: ${self.balance}")
        return {"success": True, "message": f"✅ Deposit of ${amount} successful", "balance": self.balance}
    
    def withdraw(self, amount):
        if amount <= 0:
            return {"success": False, "message": "❌ Amount must be positive"}
        if amount > self.balance:
            return {"success": False, "message": f"❌ INSUFFICIENT BALANCE. You have: ${self.balance}"}
        self.balance -= amount
        self.transactions.append(f"WITHDRAWAL: -${amount} - Balance: ${self.balance}")
        return {"success": True, "message": f"✅ Withdrawal of ${amount} successful", "balance": self.balance}
    
    def get_balance(self):
        return self.balance
    
    def get_transactions(self):
        return self.transactions