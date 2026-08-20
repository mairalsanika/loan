from LoanProcessingSystem import LoanProcessingSystem

loan = LoanProcessingSystem()

print("QA TESTING")

print("Test 1: Minimum Age")
loan.process_loan()

print("Test 2: Credit Score")
loan.process_loan()

print("Test 3: Salary")
loan.process_loan()

print("Test 4: Loan Amount")
loan.process_loan()

print("Test 5: EMI Calculation")
loan.process_loan()

print("All tests completed")