from models.account import SavingsAccount
from utils.validators import Validators

class AccountService:
    
    def __init__(self):
        self.accounts = {}
    
    def create_account(self, account_number, owner_name, initial_balance=0.0):
        is_valid, message = Validators.validate_account_number(account_number)
        if not is_valid:
            return {"success": False, "message": message}
        
        is_valid, message = Validators.validate_owner_name(owner_name)
        if not is_valid:
            return {"success": False, "message": message}
        
        if account_number in self.accounts:
            return {"success": False, "message": "❌ Account number already exists"}
        
        if initial_balance > 0:
            is_valid, message, valid_amount = Validators.validate_amount(initial_balance)
            if not is_valid:
                return {"success": False, "message": message}
            initial_balance = valid_amount
        
        account = SavingsAccount(account_number, owner_name, initial_balance)
        self.accounts[account_number] = account
        
        return {"success": True, "message": "✅ Account created successfully", "account": account}
    
    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return {"success": False, "message": "❌ Account not found"}
        
        is_valid, message, valid_amount = Validators.validate_amount(amount)
        if not is_valid:
            return {"success": False, "message": message}
        
        account = self.accounts[account_number]
        return account.deposit(valid_amount)
    
    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return {"success": False, "message": "❌ Account not found"}
        
        account = self.accounts[account_number]
        
        is_valid, message, valid_amount = Validators.validate_withdrawal(amount, account.get_balance())
        if not is_valid:
            return {"success": False, "message": message}
        
        return account.withdraw(valid_amount)
    
    def get_balance(self, account_number):
        if account_number not in self.accounts:
            return {"success": False, "message": "❌ Account not found"}
        
        account = self.accounts[account_number]
        return {"success": True, "balance": account.get_balance()}
    
    def get_all_accounts(self):
        return list(self.accounts.values())