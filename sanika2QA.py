from OrderManagement import process_order

print("===== ORDER MANAGEMENT QA TESTING =====")

# 1. Single product
print("Test 1:", process_order("P101", "Electronics", 1, 1000, "NONE", 18))

# 2. Multiple products
print("Test 2:", process_order("P102", "Clothing", 5, 500, "NONE", 5))

# 3. Zero quantity
print("Test 3:", process_order("P103", "Books", 0, 500, "NONE", 5))

# 4. Negative quantity
print("Test 4:", process_order("P104", "Books", -2, 500, "NONE", 5))

# 5. Invalid product
print("Test 5:", process_order("X999", "Books", 2, 500, "NONE", 5))

# 6. Out of stock
print("Test 6:", process_order("P999", "Electronics", 2, 1000, "NONE", 18))

# 7. Invalid coupon
print("Test 7:", process_order("P105", "Books", 2, 500, "ABC", 5))

# 8. SAVE10 coupon
print("Test 8:", process_order("P106", "Clothing", 2, 1000, "SAVE10", 5))

# 9. SAVE20 coupon
print("Test 9:", process_order("P107", "Electronics", 2, 2000, "SAVE20", 18))

# 10. Electronics discount
print("Test 10:", process_order("P108", "Electronics", 2, 1000, "NONE", 18))

# 11. Clothing discount
print("Test 11:", process_order("P109", "Clothing", 2, 1000, "NONE", 5))

# 12. Books discount
print("Test 12:", process_order("P110", "Books", 2, 1000, "NONE", 5))

# 13. Bulk order
print("Test 13:", process_order("P111", "Books", 10, 500, "NONE", 5))

# 14. Bulk + coupon
print("Test 14:", process_order("P112", "Clothing", 15, 500, "SAVE10", 5))

# 15. Maximum discount
print("Test 15:", process_order("P113", "Electronics", 20, 1000, "SAVE20", 18))

# 16. GST calculation
print("Test 16:", process_order("P114", "Electronics", 2, 3000, "NONE", 18))

# 17. Free shipping
print("Test 17:", process_order("P115", "Books", 10, 600, "NONE", 5))

# 18. Low value shipping
print("Test 18:", process_order("P116", "Books", 1, 100, "NONE", 5))

# 19. Large order
print("Test 19:", process_order("P117", "Clothing", 25, 1000, "SAVE20", 5))

# 20. Another normal order
print("Test 20:", process_order("P118", "Electronics", 3, 1500, "SAVE10", 18))

print("===== QA TESTING COMPLETED =====")