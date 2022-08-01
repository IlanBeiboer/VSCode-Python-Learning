age = 22
if age >= 18:
    message = 'Eligible'
else:
    message = 'Not Eligible'

# This is the same
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

age = 22
if age >= 18 and age < 65:
    print("yes")

# This is the same
if 18 <= age < 65:
    print("yes")