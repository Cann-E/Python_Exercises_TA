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

def water_reminder(hours):
    while hours>0:
        print(f"{hours} hours left! Time To Drink Water")
        hours-=1

water_reminder(10)



# 6. Split the Bill

def split_bill(total_amount,num_people):
    each_pay=total_amount/num_people
    return each_pay

print("Each Need to pay: ",split_bill(100,8) ,"$")

# 7. Travel Time Calculator

def travel_time(distance,speed):
    time=distance/speed
    return time

print("Time takes to travel is: ",travel_time(100,80),"hrs")

# 8. Check Movie Eligibility

def is_movie_allowed(age):
    if  age>=13:
        print("You can Watch the movie!")
    else:
        print("Your not old enough!")
        
is_movie_allowed(13)
is_movie_allowed(7)

# 9. Cooking Timer

def set_timer(minutes):
    print(f"Your timer is set to {minutes}")
    
set_timer(60)

# 10. Discount Calculator

def calculate_discount(price,discount_percentage):
    discount=price*discount_percentage
    total=price-discount
    return total

print("Discounted price is :",calculate_discount(100,0.20),"$")

