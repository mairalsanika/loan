from AirlineReservation import book_flight, cancel_booking

print("===== AIRLINE QA TESTING =====")


print("Test 1")
book_flight("AI101", "Rahul", "Adult",
            "Economy", 20, 10, 30)


print("Test 2")
book_flight("AI101", "Rahul", "Adult",
            "Economy", 20, 10, 30)
print("Test 3")
fare = book_flight("AI102", "Priya", "Adult",
                   "Business", 10, 10, 20)
cancel_booking(fare)


print("Test 4")
cancel_booking(1000)


print("Test 5")
book_flight("AI103", "Amit", "Adult",
            "Economy", 0, 10, 20)

print("Test 6")
book_flight("AI104", "", "Adult",
            "Economy", 10, 10, 20)

print("Test 7")
book_flight("AI105", "Neha", "Adult",
            "Economy", 10, 25, 20)

print("Test 8")
book_flight("AI106", "Ravi", "Student",
            "Economy", 10, 10, 20)

# 9. Senior passenger
print("Test 9")
book_flight("AI107", "Sita", "Senior",
            "Business", 10, 10, 20)

# 10. First Class
print("Test 10")
book_flight("AI108", "Karan", "Adult",
            "First", 10, 10, 20)

# 11. Low seat dynamic pricing
print("Test 11")
book_flight("AI109", "Riya", "Adult",
            "Economy", 3, 10, 20)

# 12. Last-minute booking
print("Test 12")
book_flight("AI110", "Arjun", "Adult",
            "Business", 10, 10, 5)

# 13. Low seats + last minute
print("Test 13")
book_flight("AI111", "Meena", "Adult",
            "First", 2, 20, 3)

# 14. Business class
print("Test 14")
book_flight("AI112", "Vijay", "Adult",
            "Business", 20, 10, 30)

# 15. First class
print("Test 15")
book_flight("AI113", "Anu", "Adult",
            "First", 20, 10, 30)

print("===== QA TESTING COMPLETED =====")