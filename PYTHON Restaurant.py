manu={
    1:"1 :pizza :  350",
    2:"2 :pasta :  60",
    3:"3 :bargar:  85",
    4:"4 :sweets:  280",
    5:"5 :soup  :  80"
}
item_price=[350,60,85,280,80]
print("\t\t\t Well come to my PHYTHON restaurant")
print("\t\t\t____________________________________")
print("\t\t\t\t\t    Food manu")
print("\t\t\t\t\t________________")
for i in manu:
    print("\t\t\t", manu[i],"\n")
item=int(input("Enter the number of item="))
total_tak=0
if item in manu:
    n=int(input("Enter the item value="))
    print(f"Your {n} item has been added to your order")
    total_tak=total_tak + (item_price[item-1] * n)
else:
    print("This item is not available")
print("The total amount=",total_tak)
