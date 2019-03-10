# 1. TASK: print "Hello World"
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello", name)	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello", name)	# with a comma
print("Hello " + str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

# NINJA BONUS
print("Hello " + str(name)) # fixes the error without using a comma

food_one = "Sushi"
food_two = "Takoyaki"
print("I love to eat {} and {}.".format(food_one, food_two))
print(f"I love to eat {food_one} and {food_two}.")

# Additional String Methods

print(str.capitalize("hello world")) # Capitalizes only the first character of a string
print(str.casefold("HelLo WoRlD")) # Aggressive version of the lower() method, lowercases all characters
