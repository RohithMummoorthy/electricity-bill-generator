id=input("Enter your Consumer ID : ")
name=str(input("Enter your Name : "))
unitsconsumed=float(input("Enter the units consumed : "))
if unitsconsumed<=100:
    price=unitsconsumed*2
    consumption="Low Consumption"
elif unitsconsumed>100 and unitsconsumed<=200:
    price=(100*2)+((unitsconsumed-100)*3)
    consumption="Moderate Consumption"
elif unitsconsumed>200:
    price=(100*2)+(100*3)+((unitsconsumed-200)*5)
    consumption="High Consumption"
a=input("Do you have Membership,If yes Enter the code,else enter no : ")
membership=list(a)
initialprice=float(price)
if a in "prime":
    discountprice=price*(10/100)
    price-=discountprice
else:
    price+=0
meter_type = 1
smart_meter_flag = meter_type & 1
manual_meter_flag = meter_type & 0
print("="*100)
print(" "*42,"ELECTRICITY BILL"," "*42)
print("="*100)
print(f"CONSUMER NAME                : {name}")
print(f"CONSUMER ID                  : {id}")
print(f"TOTAL UNITS CONSUMED         : {unitsconsumed}")
print(f"REMARKS                      : {consumption}")
print(f"INITIAL AMOUNT               : {initialprice}")
print(f"FINAL PRICE(IF ANY DISCOUNT) : {price}")
print(f"SMART METER ACTIVE           : {smart_meter_flag}")
print(f"MANUAL METER                 : {manual_meter_flag}")
print("="*100)