class Validators:
    
    @staticmethod
    def validate_account_number(account_number):
        if not account_number or len(account_number.strip()) < 4:
            return False, "❌ Account number must be at least 4 characters"
        
        account_number = account_number.replace(" ", "")
        
        if not account_number.isdigit():
            return False, "❌ Account number must contain ONLY numbers (no letters)"
        
        return True, "✅ Valid account number"
    
    @staticmethod
    def validate_owner_name(name):
        if not name or len(name.strip()) < 2:
            return False, "❌ Name must be at least 2 characters"
        
        if not all(c.isalpha() or c.isspace() for c in name):
            return False, "❌ Name can only contain letters and spaces (no numbers)"
        
        return True, "✅ Valid name"
    
    @staticmethod
    def validate_amount(amount):
        try:
            amount = float(amount)
        except ValueError:
            return False, "❌ Must be a valid number", None
        
        if amount <= 0:
            return False, "❌ Amount must be positive", None
        
        if amount > 10000:
            return False, "❌ Maximum amount is $10,000", None
        
        return True, "✅ Valid amount", amount
    
    @staticmethod
    def validate_withdrawal(amount, balance):
        is_valid, message, valid_amount = Validators.validate_amount(amount)
        if not is_valid:
            return False, message, None
        
        if valid_amount > balance:
            return False, f"❌ INSUFFICIENT BALANCE. You have: ${balance:.2f}", None
        
        if valid_amount > 5000:
            return False, "❌ Maximum withdrawal is $5,000", None
        
        return True, "✅ Valid withdrawal", valid_amount