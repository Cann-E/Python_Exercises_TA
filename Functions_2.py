# 1. Greet a Friend

def greet(name):
    print(f"Hey {name},how are you doing today?")
    
greet("Can")

# 2. Calculate Total Cost

def calculate_total(price,quantity):
    total=price*quantity
    print(f"Total Cost is : {total} $")
    return total

    
calculate_total(30,5)

# 3. Tip Calculator

def calculate_tip(bill_amount,tip_percentage):
    tip=bill_amount*tip_percentage
    return tip
    
    
print("Total tip for your bill is: ",calculate_tip(93,0.18),"$")

# 4. Shopping List Length

cart=[]
def shopping_list_lenght(items):
    cart.append(items)
    print(cart)
    return (len(cart))

print(shopping_list_lenght("apple"))
print(shopping_list_lenght("pear"))
print(shopping_list_lenght("watermelon"))
    


# 5. Daily Water Reminder



# 6. Split the Bill
# 7. Travel Time Calculator
# 8. Check Movie Eligibility
# 9. Cooking Timer
# 10. Discount Calculator