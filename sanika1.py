class LoanProcessingSystem:

    def process_loan(self):
        customer_id = "C101"
        age = 30
        salary = 50000
        existing_loan = 50000
        credit_score = 750
        employment = "Salaried"
        requested_loan = 1000000
        tenure = 5

        dti = (existing_loan / (salary * 12)) * 100
        eligible_loan = salary * 12 * 5

        if credit_score >= 750:
            interest = 8
        elif credit_score >= 650:
            interest = 10
        else:
            interest = 13

        emi = requested_loan * (1 + interest / 100) / (tenure * 12)

        if age >= 21 and age <= 60 and salary > 0 and credit_score >= 600:
            status = "Approved"
        else:
            status = "Rejected"

        print("Customer ID:", customer_id)
        print("DTI:", round(dti, 2), "%")
        print("Eligible Loan:", eligible_loan)
        print("Interest Rate:", interest, "%")
        print("EMI:", round(emi, 2))
        print("Employment:", employment)
        print("Status:", status)


loan = LoanProcessingSystem()
loan.process_loan()