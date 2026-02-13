class SavingsAccount:
    
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
        
        if initial_balance > 0:
            self.transactions.append(f"INITIAL DEPOSIT: +${initial_balance} - Balance: ${initial_balance}")
    
    # 🟢 SOLO DEPOSIT - FEATURE/DEPOSIT
    def deposit(self, amount):
        if amount <= 0:
            return {"success": False, "message": "❌ Amount must be positive"}
        
        self.balance += amount
        self.transactions.append(f"DEPOSIT: +${amount} - Balance: ${self.balance}")
        
        return {"success": True, "message": f"✅ Deposit of ${amount} successful", "balance": self.balance}
    
    # ❌ OTROS MÉTODOS VACÍOS (SOLO ESTRUCTURA)
    def withdraw(self, amount):
        pass
    
    def get_balance(self):
        pass
    
    def get_transactions(self):
        return self.transactions