cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")


answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() +", you can post a response if you wish.")


age = 25
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


age_1 = 12
if age_1 < 4:
    print("Your admission cost is $0.")
elif age_1 < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished makeing your pizza!")