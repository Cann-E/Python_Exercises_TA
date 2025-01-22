#Functions Practice

#1 Basic Function
def greet(name):
    print(f"Greetings {name}")
    
greet("Can")


# 2 Sum and Product

def sum_and_product(a,b):
    total_sum=a+b
    total_product=a*b
    return total_sum,total_product

print(sum_and_product(13,37))

# 3 Palindrome Checker

def is_palindrome(word):
    word=word.lower()
    if word == word[::-1]:
        print(f"{word} Is a Palindrome!")
    else:
        print(f"{word} Not Palindrome!")
        
is_palindrome("can")
is_palindrome("mom")

# 4 Factorial Calculator

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1) #recursive case
        
        
print(factorial(5))

# 5 Number Guessing Game

from random import *

def guess_number():
    tries=1
    random=randint(1,10)
    print(random)
    guess=int(input("Please Enter your guess Number(1-10): "))
    while guess != random:
        guess=int(input(f"{guess} is not correct try again: "))
        tries+=1
        if guess == random:
            print(f"{guess} is Correct")
            tries+=1
            break
    print(f"{random} was the random number and it took you {tries} tries!")
    
        
guess_number()

        

# 6 Fibonacci Sequence

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2) #recursion using the function itself
    
    
print(fibonacci(10))
    

# 7 Odd or Even

def odd_even(number):
    if number%2==0:
        print("Even!")
    else:
        print("Odd!")
        
odd_even(11)
odd_even(20)

# 8 Word Counter

def count_word():
    sentence=input("Enter your sentence: ")
    word_count=len(sentence.split(" ")) # Split the sentence into words and count them
    return sentence,word_count # Return both the sentence and the word count

sentence,count=count_word() #Capture returned Values
print(f"Word count for '{sentence}' is: {count}")


# 9 Nested Functions

def outer_function(x): #if wanted to give another value inside def outer_function(x,y)
    def inner_function(y):
        return y**2
    return x+inner_function(x)


print(outer_function(5))

# 10 Timer Function

from time import time, sleep

def countdown_timer():
    start_time = int(input("Enter 1 to start the timer or 2 to end: "))
    if start_time == 1:
        start_ = time()  
        print("Timer started...")
        input("Press Enter to stop the timer.")  
        stop_ = time()  
        time_passed = stop_ - start_
        print(f"Seconds passed: {round(time_passed, 2)}")
    else:
        print("Timer not started.")

countdown_timer()



