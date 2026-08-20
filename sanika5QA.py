from DigitalWallet import Wallet

print("===== WALLET SECURITY QA =====")

# 1. Normal transaction
print("\nTest 1 - Normal transaction")
w1 = Wallet("Amit", 10000, 1234)
print(w1.deposit(1000))

# 2. Insufficient balance
print("\nTest 2 - Insufficient balance")
w2 = Wallet("Riya", 5000, 1234)
print(w2.withdraw(8000, 1234))

# 3. Daily limit
print("\nTest 3 - Daily limit")
w3 = Wallet("Raj", 10000, 1234)
print(w3.withdraw(6000, 1234))
print(w3.withdraw(5000, 1234))

# 4. Multiple failed PINs
print("\nTest 4 - Multiple failed PINs")
w4 = Wallet("Neha", 10000, 1234)
print(w4.withdraw(1000, 1111))
print(w4.withdraw(1000, 2222))
print(w4.withdraw(1000, 3333))

# 5. Suspicious large transaction
print("\nTest 5 - Suspicious transaction")
w5 = Wallet("Karan", 20000, 1234)
print(w5.withdraw(15000, 1234))

# 6. Duplicate transaction
print("\nTest 6 - Duplicate transaction")
w6 = Wallet("Sita", 10000, 1234)
print(w6.transfer(2000, 1234))
print(w6.transfer(2000, 1234))

# 7. Negative amount
print("\nTest 7 - Negative amount")
w7 = Wallet("Vijay", 10000, 1234)
print(w7.deposit(-500))

# 8. Zero amount
print("\nTest 8 - Zero amount")
print(w7.withdraw(0, 1234))

# 9. Too many transactions
print("\nTest 9 - Too many transactions")
w8 = Wallet("Anu", 30000, 1234)
print(w8.deposit(1000))
print(w8.deposit(1000))
print(w8.deposit(1000))
print(w8.deposit(1000))
print(w8.transfer(1000, 1234))
print(w8.transfer(1000, 1234))

# 10. Balance verification
print("\nTest 10 - Balance verification")
w9 = Wallet("Arjun", 5000, 1234)
w9.deposit(2000)
w9.show_balance()

print("\n===== QA TESTING COMPLETED =====")