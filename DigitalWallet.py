class Wallet:

    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        self.transactions = []
        self.failed_pins = 0

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"

        self.balance += amount
        self.transactions.append(amount)
        return "Deposit successful"

    def withdraw(self, amount, pin):
        if amount <= 0:
            return "Invalid amount"

        if pin != self.pin:
            self.failed_pins += 1

            if self.failed_pins >= 3:
                return "Suspicious: Multiple failed PIN attempts"

            return "Wrong PIN"

        if amount > self.balance:
            return "Insufficient balance"

        self.balance -= amount
        self.transactions.append(-amount)

        # Basic fraud detection
        if amount > 10000:
            return "Withdrawal successful - Suspicious large transaction"

        return "Withdrawal successful"

    def transfer(self, amount, pin):
        if amount <= 0:
            return "Invalid amount"

        if pin != self.pin:
            self.failed_pins += 1
            return "Wrong PIN"

        if amount > self.balance:
            return "Insufficient balance"

        self.balance -= amount
        self.transactions.append(-amount)

        if amount > 10000:
            return "Transfer successful - Suspicious transaction"

        if len(self.transactions) > 5:
            return "Transfer successful - Suspicious: Too many transactions"

        return "Transfer successful"

    def show_balance(self):
        print("Balance:", self.balance)

    def history(self):
        print("Transaction History:", self.transactions)


# Account creation
wallet = Wallet("Rahul", 15000, 1234)

print("Account created for:", wallet.name)

# Normal transactions
print(wallet.deposit(2000))
print(wallet.withdraw(1000, 1234))
print(wallet.transfer(2000, 1234))

# Fraud detection
print(wallet.withdraw(12000, 1234))

wallet.show_balance()
wallet.history()