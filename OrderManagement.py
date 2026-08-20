def process_order(product_id, category, quantity, price, coupon, tax):

    if quantity <= 0:
        return "Invalid quantity"

    if product_id == "P999":
        return "Out of stock"

    if not product_id.startswith("P"):
        return "Invalid product"

    subtotal = quantity * price

    if category == "Electronics":
        discount = subtotal * 0.10
    elif category == "Clothing":
        discount = subtotal * 0.15
    elif category == "Books":
        discount = subtotal * 0.05
    else:
        discount = 0

    if quantity >= 10:
        discount += subtotal * 0.05

    if coupon == "SAVE10":
        discount += subtotal * 0.10
    elif coupon == "SAVE20":
        discount += subtotal * 0.20
    elif coupon != "NONE":
        return "Invalid coupon"

    # Maximum discount = 30%
    if discount > subtotal * 0.30:
        discount = subtotal * 0.30

    gst = (subtotal - discount) * tax / 100

    if subtotal >= 5000:
        shipping = 0
    else:
        shipping = 100

    final_amount = subtotal - discount + gst + shipping

    return final_amount


# Normal examples
print("Order 1:", process_order("P101", "Electronics", 2, 1000, "NONE", 18))
print("Order 2:", process_order("P102", "Clothing", 5, 800, "SAVE10", 5))
print("Order 3:", process_order("P103", "Books", 10, 500, "SAVE20", 5))