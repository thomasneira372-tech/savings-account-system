class SavingsAccount:
    
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance
        self.transactions = []
        
        if initial_balance > 0:
            self.transactions.append(f"INITIAL DEPOSIT: +${initial_balance} - Balance: ${initial_balance}")
    
    # ❌ DEPOSIT VACÍO
    def deposit(self, amount):
        pass
    
    # ❌ WITHDRAW VACÍO
    def withdraw(self, amount):
        pass
    
    # 🟢 SOLO GET_BALANCE - FEATURE/BALANCE
    def get_balance(self):
        return self.balance
    
    def get_transactions(self):
        return self.transactions