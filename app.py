special_characters = "!@#$%^&*()-_=+[];:'<>,./?"

print("Welcome to your password generator. Lets get started!")

street = input("\nWhat street did you live on as a child?\n")
pet = input("What is your pets name?\n")
color = input("What is your favorite color?\n")
food = input("What is your favorite food?\n")
month = input("What month were you born?\n")

random_index = len(street) if len(street) <= 24 else -1

password = special_characters[random_index - 1] + str(len(month)) + pet.upper() + special_characters[random_index + 1] + color.lower() + str(len(food)) + special_characters[random_index]

print("Your password is:", password)
