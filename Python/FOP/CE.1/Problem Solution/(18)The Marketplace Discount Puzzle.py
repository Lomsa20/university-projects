# Ask the user for their customer type and purchase amount
ctype = input("Customer type (regular/member/vip): ").strip().lower()
amount = float(input("Purchase amount (€): "))

# Start with no discount
discount = 0.0

# Check what type of customer it is
if ctype == "regular":
    discount = 0.0  # Regular customers get no discount

elif ctype == "member":
    # Members get a discount depending on purchase size
    if amount >= 500:
        discount = 0.10  # 10% off for big purchases
    elif amount >= 100:
        discount = 0.05  # 5% off for medium purchases

elif ctype == "vip":
    # VIP customers get the biggest discounts
    if amount >= 500:
        discount = 0.20  # 20% off for large purchases
    elif amount >= 100:
        discount = 0.10  # 10% off for medium purchases

else:
    # If input type doesn’t match any known category
    print("Unknown customer type")

# Compute the final price after discount
final_price = amount * (1 - discount)

# Display the result formatted to 2 decimal places
print(f"Final price after discount: €{final_price:.2f}")
