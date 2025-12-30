consumer_id = input("Enter your Consumer ID: ")
name = input("Enter your Name: ")
units_consumed = float(input("Enter the units consumed: "))

# Bill calculation
if units_consumed <= 100:
    price = units_consumed * 2
    consumption = "Low Consumption"
elif units_consumed <= 200:
    price = (100 * 2) + ((units_consumed - 100) * 3)
    consumption = "Moderate Consumption"
else:
    price = (100 * 2) + (100 * 3) + ((units_consumed - 200) * 5)
    consumption = "High Consumption"

initial_price = price

# Membership discount
membership = input("Do you have Prime membership? (yes/no): ")
if membership.lower() == "yes":
    discount = price * 0.10
    price -= discount

# Meter type
smart_meter = True
manual_meter = False

# Output
print("=" * 80)
print(" " * 30 + "ELECTRICITY BILL")
print("=" * 80)
print(f"CONSUMER NAME        : {name}")
print(f"CONSUMER ID          : {consumer_id}")
print(f"UNITS CONSUMED       : {units_consumed}")
print(f"CONSUMPTION TYPE     : {consumption}")
print(f"INITIAL AMOUNT       : ₹{initial_price:.2f}")
print(f"FINAL AMOUNT         : ₹{price:.2f}")
print(f"SMART METER          : {smart_meter}")
print(f"MANUAL METER         : {manual_meter}")
print("=" * 80)
