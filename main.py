"""
SAVINGS ACCOUNT SYSTEM
Author: [Your name]

====================================
TODOS LOS COMENTARIOS ESTÁN EN ESPAÑOL
El código está 100% en inglés (requisito)
====================================
"""

# =======================================================
# CLASE 1: SAVINGS ACCOUNT
# =======================================================
# Esta clase es el corazón del programa
# Aquí guardo: número de cuenta, nombre del dueño, saldo y movimientos
# =======================================================

class SavingsAccount:
    
    # ---------------------------------------------------
    # CONSTRUCTOR - Se ejecuta cuando creo una cuenta nueva
    # ---------------------------------------------------
    def __init__(self, account_number, owner_name, initial_balance=0.0):
        self.account_number = account_number    # Número de cuenta único
        self.owner_name = owner_name            # Nombre del titular
        self.balance = initial_balance          # Saldo inicial (0 por defecto)
        self.transactions = []                 # Lista para guardar todos los movimientos
    
    # ---------------------------------------------------
    # MÉTODO: deposit - Para meter dinero a la cuenta
    # ---------------------------------------------------
    # Validación: El monto debe ser positivo
    # Si es válido, se suma al saldo y se guarda el movimiento
    def deposit(self, amount):
        # VALIDACIÓN: No permitir montos negativos o cero
        if amount <= 0:
            return {"success": False, "message": "❌ Amount must be positive"}
        
        # PROCESO: Sumar el dinero al saldo
        self.balance += amount
        
        # REGISTRO: Guardar esta operación en el historial
        self.transactions.append(f"DEPOSIT: +${amount} - Balance: ${self.balance}")
        
        # RESULTADO: Devolver que todo salió bien
        return {"success": True, "message": f"✅ Deposit of ${amount} successful", "balance": self.balance}
    
    # ---------------------------------------------------
    # MÉTODO: withdraw - Para sacar dinero de la cuenta
    # ---------------------------------------------------
    # REQUISITO PRINCIPAL DEL BANCO: Validar SALDO INSUFICIENTE
    # También valido que el monto sea positivo
    def withdraw(self, amount):
        # VALIDACIÓN 1: No permitir montos negativos o cero
        if amount <= 0:
            return {"success": False, "message": "❌ Amount must be positive"}
        
        # VALIDACIÓN 2: SALDO INSUFICIENTE - ESTO ES LO QUE PIDEN
        if amount > self.balance:
            return {"success": False, "message": f"❌ INSUFFICIENT BALANCE. You have: ${self.balance}"}
        
        # PROCESO: Restar el dinero del saldo
        self.balance -= amount
        
        # REGISTRO: Guardar esta operación en el historial
        self.transactions.append(f"WITHDRAWAL: -${amount} - Balance: ${self.balance}")
        
        # RESULTADO: Devolver que todo salió bien
        return {"success": True, "message": f"✅ Withdrawal of ${amount} successful", "balance": self.balance}
    
    # ---------------------------------------------------
    # MÉTODO: get_balance - Consultar saldo actual
    # ---------------------------------------------------
    # Solo devuelve el saldo que tiene la cuenta
    def get_balance(self):
        return self.balance
    
    # ---------------------------------------------------
    # MÉTODO: get_transactions - Ver todo el historial
    # ---------------------------------------------------
    # Devuelve la lista completa de movimientos
    def get_transactions(self):
        return self.transactions


# =======================================================
# CLASE 2: AccountService
# =======================================================
# Esta clase maneja MÚLTIPLES cuentas a la vez
# Puedo crear varias cuentas y operar con cualquiera
# =======================================================

class AccountService:
    
    # ---------------------------------------------------
    # CONSTRUCTOR - Inicializo el servicio sin cuentas
    def __init__(self):
        self.accounts = {}  # Diccionario: clave = número de cuenta, valor = objeto cuenta
    
    # ---------------------------------------------------
    # MÉTODO: create_account - Crear una cuenta nueva
    # ---------------------------------------------------
    def create_account(self, account_number, owner_name, initial_balance=0.0):
        # VALIDACIÓN: No puedo crear dos cuentas con el mismo número
        if account_number in self.accounts:
            return {"success": False, "message": "❌ Account number already exists"}
        
        # Creo la cuenta usando la clase SavingsAccount
        account = SavingsAccount(account_number, owner_name, initial_balance)
        
        # Guardo la cuenta en el diccionario usando su número como clave
        self.accounts[account_number] = account
        
        return {"success": True, "message": "✅ Account created", "account": account}
    
    # ---------------------------------------------------
    # MÉTODO: deposit - Depositar en una cuenta específica
    # ---------------------------------------------------
    def deposit(self, account_number, amount):
        # VALIDACIÓN: La cuenta debe existir
        if account_number not in self.accounts:
            return {"success": False, "message": "❌ Account not found"}
        
        # Busco la cuenta y hago el depósito
        account = self.accounts[account_number]
        return account.deposit(amount)
    
    # ---------------------------------------------------
    # MÉTODO: withdraw - Retirar de una cuenta específica
    # ---------------------------------------------------
    def withdraw(self, account_number, amount):
        # VALIDACIÓN: La cuenta debe existir
        if account_number not in self.accounts:
            return {"success": False, "message": "❌ Account not found"}
        
        # Busco la cuenta y hago el retiro
        account = self.accounts[account_number]
        return account.withdraw(amount)
    
    # ---------------------------------------------------
    # MÉTODO: get_balance - Consultar saldo de una cuenta
    # ---------------------------------------------------
    def get_balance(self, account_number):
        # VALIDACIÓN: La cuenta debe existir
        if account_number not in self.accounts:
            return {"success": False, "message": "❌ Account not found"}
        
        # Busco la cuenta y obtengo su saldo
        account = self.accounts[account_number]
        return {"success": True, "balance": account.get_balance()}
    
    # ---------------------------------------------------
    # MÉTODO: get_all_accounts - Listar todas las cuentas
    # ---------------------------------------------------
    def get_all_accounts(self):
        return list(self.accounts.values())


# =======================================================
# PROGRAMA PRINCIPAL - main()
# =======================================================
# Aquí empieza TODO cuando ejecuto el archivo
# Esta función muestra el menú y maneja la interacción con el usuario
# =======================================================

def main():
    # Encabezado del programa
    print("\n" + "="*50)
    print("🏦 SAVINGS ACCOUNT SYSTEM")
    print("="*50)
    
    # Creo el servicio que va a administrar todas las cuentas
    service = AccountService()
    
    # Variable para guardar la cuenta que estoy usando actualmente
    current_account = None
    
    # Bucle infinito - Solo se rompe cuando el usuario elige salir
    while True:
        # MENÚ PRINCIPAL - Opciones que ve el usuario
        print("\n📋 MAIN MENU:")
        print("1. Create new account")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Check balance")
        print("5. View transaction history")
        print("6. View all accounts")
        print("7. Exit")
        
        # Pido la opción al usuario
        option = input("\nChoose an option (1-7): ")
        
        # ---------------------------------------------------
        # OPCIÓN 1: Crear cuenta nueva
        # ---------------------------------------------------
        if option == "1":
            print("\n--- NEW ACCOUNT ---")
            number = input("Account number: ")
            name = input("Owner name: ")
            
            # Pido saldo inicial, si no ingresa nada es 0
            try:
                initial_balance = float(input("Initial balance: $") or "0")
            except:
                initial_balance = 0.0
            
            # Llamo al servicio para crear la cuenta
            result = service.create_account(number, name, initial_balance)
            print(result["message"])
            
            # Si se creó bien, la selecciono automáticamente
            if result["success"]:
                current_account = result["account"]
        
        # ---------------------------------------------------
        # OPCIÓN 2: Depositar dinero
        # ---------------------------------------------------
        elif option == "2":
            # Verifico que haya una cuenta seleccionada
            if not current_account:
                print("❌ Please create or select an account first")
                continue
            
            print(f"\n--- DEPOSIT TO {current_account.account_number} ---")
            print(f"Current balance: ${current_account.get_balance()}")
            
            # Pido el monto a depositar
            try:
                amount = float(input("Amount to deposit: $"))
                result = service.deposit(current_account.account_number, amount)
                print(result["message"])
                if result["success"]:
                    print(f"New balance: ${result['balance']}")
            except:
                print("❌ Invalid amount")
        
        # ---------------------------------------------------
        # OPCIÓN 3: Retirar dinero (AQUÍ ESTÁ LA VALIDACIÓN IMPORTANTE)
        # ---------------------------------------------------
        elif option == "3":
            # Verifico que haya una cuenta seleccionada
            if not current_account:
                print("❌ Please create or select an account first")
                continue
            
            print(f"\n--- WITHDRAW FROM {current_account.account_number} ---")
            print(f"Available balance: ${current_account.get_balance()}")
            
            # Pido el monto a retirar
            try:
                amount = float(input("Amount to withdraw: $"))
                # ESTA LÍNEA VALIDA EL SALDO INSUFICIENTE (requisito)
                result = service.withdraw(current_account.account_number, amount)
                print(result["message"])  # Si no tiene saldo, aquí sale el error
                if result["success"]:
                    print(f"New balance: ${result['balance']}")
            except:
                print("❌ Invalid amount")
        
        # ---------------------------------------------------
        # OPCIÓN 4: Consultar saldo
        # ---------------------------------------------------
        elif option == "4":
            # Verifico que haya una cuenta seleccionada
            if not current_account:
                print("❌ Please create or select an account first")
                continue
            
            print(f"\n--- BALANCE OF {current_account.account_number} ---")
            print(f"Owner: {current_account.owner_name}")
            print(f"Current balance: ${current_account.get_balance():.2f}")
        
        # ---------------------------------------------------
        # OPCIÓN 5: Ver historial de transacciones
        # ---------------------------------------------------
        elif option == "5":
            # Verifico que haya una cuenta seleccionada
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
        
        # ---------------------------------------------------
        # OPCIÓN 6: Ver todas las cuentas
        # ---------------------------------------------------
        elif option == "6":
            print("\n--- ALL ACCOUNTS ---")
            accounts = service.get_all_accounts()
            
            if not accounts:
                print("No accounts created")
            else:
                for i, account in enumerate(accounts, 1):
                    print(f"{i}. {account.account_number} - {account.owner_name} - ${account.get_balance():.2f}")
        
        # ---------------------------------------------------
        # OPCIÓN 7: Salir del programa
        # ---------------------------------------------------
        elif option == "7":
            print("\n👋 Thank you for using Savings Account System!")
            print("   Goodbye!")
            break
        
        # ---------------------------------------------------
        # Opción inválida
        # ---------------------------------------------------
        else:
            print("❌ Invalid option. Please choose 1-7")
        
        # Pausa para que el usuario pueda leer los resultados
        if option != "7":
            input("\nPress Enter to continue...")


# =======================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# =======================================================
# Esta línea verifica si el archivo se está ejecutando directamente
# Si es así, llama a la función main()
# =======================================================
if __name__ == "__main__":
    main()