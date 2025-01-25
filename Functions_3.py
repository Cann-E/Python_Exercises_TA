
# 1. Library Late Fee Calculator
# Write a function `calculate_late_fee(days_late)` that takes the number of days 
# a book is overdue and returns the late fee. Assume:
# - $0.25 per day for the first 7 days.
# - $0.50 per day after 7 days.


def calculate_late_fee(days_late):
    while True:
        if days_late<=7:
            fee=days_late*0.25            
        else:
            fee=days_late*0.50
            
        return fee   
        
        
print("fee is :",calculate_late_fee(6),"$")
print("fee is :",calculate_late_fee(12),"$")



# 2. Grocery Store Receipt
# Write a function `generate_receipt(items, prices)` that takes two lists:
# - `items`: A list of item names.
# - `prices`: A corresponding list of item prices.
# The function should print a receipt, including the total amount. Example:
# Apple - $1.50
# Banana - $0.75
# Total: $2.25


items = []  
prices = []  

def generate_receipt(item, price):  
    items.append(item)  
    prices.append(price)  

    print("Receipt:")
    total = 0  
    for i in range(len(items)):  # Iterate through indices of the items list
        print(f"{items[i]} - ${prices[i]:.2f}")  # Print each item and price
        total += prices[i]  # Accumulate the total price
    print(f"Total: ${total:.2f}")  


generate_receipt("apple", 1.50)
generate_receipt("watermelon", 5.50)


    





# 3. Email Validator
# Write a function `is_valid_email(email)` that takes an email address and:
# - Returns `True` if it contains `@` and a domain (e.g., `.com`, `.org`).
# - Returns `False` otherwise.

def is_valid_email(email):
    valid = "@"
    valid2 = ".com"
 
    if valid in email and valid2 in email:
        return True
    else:
        return False

print(is_valid_email("cann0211@gmail.com"))  
print(is_valid_email("cann0211.com"))       







# 4. Order Confirmation System
# Write a function `confirm_order(order_number, customer_name)` that takes an order number 
# and a customer name, and prints a confirmation message:
# Thank you, [customer_name]. Your order #[order_number] is being processed!


def confirm_order(order_number, customer_name):
    print(f"Thank you, {customer_name}. Your order #{order_number} is being processed!")
    
confirm_order(1112345,"Can Ercan")



# 5. Event RSVP Counter
# Write a function `rsvp_count(responses)` that takes a list of responses (`"yes"`, `"no"`, `"maybe"`) and:
# - Counts how many people said `"yes"`, `"no"`, and `"maybe"`.
# - Prints the counts in a friendly message.

def rsvp_count():
    responses = {"Y": 0, "N": 0, "MAYBE": 0}  # Dictionary to track counts
    answer = []  
    
    while True:
        response = input("Please RSVP to the meeting (Y/N/MAYBE or Q to quit): ").upper()
        if response == "Q":  
            break
        elif response in ["Y", "N", "MAYBE"]:
            responses[response] += 1  # Increment the count for the response
            answer.append(response)  # Add response to the list
        else:
            print("Invalid input. Please enter Y, N, MAYBE, or Q to quit.")
    
    print(f"\nRSVP Summary:")
    print(f"Yes: {responses['Y']} people")
    print(f"No: {responses['N']} people")
    print(f"Maybe: {responses['MAYBE']} people")
    print(f"Total RSVP: {sum(responses.values())} people")

rsvp_count()

        

        

# 6. Hotel Room Price Calculator
# Write a function `calculate_room_price(nights, room_type)` that:
# - Calculates the total cost of staying at a hotel based on the room type:
#   - `"single"`: $50/night.
#   - `"double"`: $75/night.
#   - `"suite"`: $120/night.



def calculate_room_price(nights,room_type):
    if room_type =="single":
        price=nights*50
        
    elif room_type =="double":
        price=nights*75
        
    elif room_type =="suite":
        price=nights*120
    print(f"{nights} nights for {room_type} is {price}$ USD")
        
    
calculate_room_price(5,"single")
calculate_room_price(9,"double")
calculate_room_price(2,"suite")




# 7. Fitness Tracker Steps Goal
# Write a function `steps_to_goal(steps_taken, goal_steps=10000)` that:
# - Takes the number of steps taken so far and calculates how many more steps are needed 
#   to reach the daily goal (default is 10,000 steps).

def steps_to_goal(steps_taken,goal_steps=10000):
    remaining=goal_steps-steps_taken
    return remaining

print(steps_to_goal(5346))
print(steps_to_goal(15000))





# 8. Packing List Helper
# Write a function `packing_list(items, days)` that:
# - Takes a list of items and the number of days for a trip.
# - Prints a suggested packing list where each item is multiplied by the number of days.
# Example:
# Shirts: 5
# Socks: 5
# Toothbrush: 1


def packing_list(items, days):
    for item in items:
        print(f"{item}: {days}")


packing_list(["Shirts", "Socks", "Pants"], 5)





# 9. Password Strength Checker
# Write a function `password_strength(password)` that:
# - Checks the strength of a password based on:
#   - Length (8+ characters).
#   - Inclusion of numbers.
#   - Inclusion of special characters (e.g., `!@#$`).
# - Prints `"Strong"`, `"Moderate"`, or `"Weak"`.


def password_strength(password):
    special_character=("!@#$")
    numbers=("1234567890")
    
    has_special=any(char in special_character for char in password)
    has_numbers=any(char in numbers for char in password)
    
    
    if len(password)>8 and has_special  and has_numbers :
        print((f"{password} is a Strong Password"))
    elif len(password)>8 and has_special :
        print(f"{password} is a moderate Password!")
    else:
        print(f"{password} is a weak password!")
        
    
        
        
        
password_strength("can1")
password_strength("can123456")
password_strength("hello@world")
password_strength("can1@!45678$")



# 10. Restaurant Waitlist Manager
# Write a function `waitlist_manager(waitlist, new_customer)` that:
# - Takes a list of current waitlisted customers and a new customer name.
# - Adds the new customer to the list and prints the updated waitlist.


def waitlist_manager(waitlist,new_customer):
    
    print(f"{waitlist} currently in waitlist.And new customer is {new_customer}")
    waitlist.append(new_customer)
    print(f"Updated Waitlist:",waitlist)
        
        
        
waitlist_manager(["asli","Lyndsey","Remy"],"can")
    
    
    
    
    
    

