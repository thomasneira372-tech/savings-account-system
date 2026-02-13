import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from services.account_service import AccountService
from utils.validators import Validators

def main():
    print("\n" + "="*50)
    print("🏦 SAVINGS ACCOUNT SYSTEM")
    print("="*50)
    
    service = AccountService()
    current_account = None
    
    while True:
        print("\n📋 MAIN MENU:")
        print("1. Create new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. View transaction history")
        print("6. View all accounts")
        print("7. Exit")
        
        option = input("\nChoose an option (1-7): ")
        
        if option == "1":
            print("\n--- NEW ACCOUNT ---")
            
            # Validar número de cuenta
            while True:
                number = input("Account number: ").strip()
                is_valid, message = Validators.validate_account_number(number)
                if is_valid:
                    break
                print(message)
            
            # Validar nombre (NO números, NO caracteres especiales)
            while True:
                name = input("Owner name: ").strip()
                is_valid, message = Validators.validate_owner_name(name)
                if is_valid:
                    break
                print(message)
            
            # Validar saldo inicial
            initial_balance = 0.0
            bal_input = input("Initial balance (press Enter for $0): $").strip()
            if bal_input:
                is_valid, message, valid_amount = Validators.validate_amount(bal_input)
                if is_valid:
                    initial_balance = valid_amount
                else:
                    print(message)
                    print("Setting initial balance to $0")
            
            # Crear cuenta
            result = service.create_account(number, name, initial_balance)
            print(result["message"])
            
            if result["success"]:
                current_account = result["account"]
        
        elif option == "2":
            if not current_account:
                print("❌ Please create or select an account first")
                continue
            
            print(f"\n--- DEPOSIT TO {current_account.account_number} ---")
            print(f"Current balance: ${current_account.get_balance():.2f}")
            
            # Validar monto a depositar
            while True:
                amount = input("Amount to deposit: $").strip()
                is_valid, message, valid_amount = Validators.validate_amount(amount)
                if is_valid:
                    break
                print(message)
            
            # Hacer depósito
            result = service.deposit(current_account.account_number, valid_amount)
            print(result["message"])
            if result["success"]:
                print(f"New balance: ${result['balance']:.2f}")
        
        elif option == "3":
            if not current_account:
                print("❌ Please create or select an account first")
                continue
            
            print(f"\n--- WITHDRAW FROM {current_account.account_number} ---")
            print(f"Available balance: ${current_account.get_balance():.2f}")
            
            # Validar monto a retirar
            while True:
                amount = input("Amount to withdraw: $").strip()
                is_valid, message, valid_amount = Validators.validate_amount(amount)
                if is_valid:
                    result = service.withdraw(current_account.account_number, valid_amount)
                    print(result["message"])
                    if result["success"]:
                        print(f"New balance: ${result['balance']:.2f}")
                    break
                else:
                    print(message)
        
        elif option == "4":
            if not current_account:
                print("❌ Please create or select an account first")
                continue
            
            print(f"\n--- BALANCE OF {current_account.account_number} ---")
            print(f"Owner: {current_account.owner_name}")
            print(f"Current balance: ${current_account.get_balance():.2f}")
        
        elif option == "5":
            if not current_account:
                print("❌ Please create or select an account first")
                continue
            
            print(f"\n--- TRANSACTION HISTORY OF {current_account.account_number} ---")
            transactions = current_account.get_transactions()
            
            if not transactions:
                print("No transactions yet")
            else:
                for i, mov in enumerate(transactions, 1):
                    print(f"{i}. {mov}")
        
        elif option == "6":
            print("\n--- ALL ACCOUNTS ---")
            accounts = service.get_all_accounts()
            
            if not accounts:
                print("No accounts created")
            else:
                for i, account in enumerate(accounts, 1):
                    print(f"{i}. {account.account_number} - {account.owner_name} - ${account.get_balance():.2f}")
        
        elif option == "7":
            print("\n👋 Thank you for using Savings Account System!")
            print("   Goodbye!")
            break
        
        else:
            print("❌ Invalid option. Please choose 1-7")
        
        if option != "7":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()