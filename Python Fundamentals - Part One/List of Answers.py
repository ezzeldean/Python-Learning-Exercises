
# 1. Comments
print("Hello World!") # Printing Hello World Message


# 2. Variables
name = "John Doe"
age = 27
print(f"My name is {name}, I'm {age} years old.") # Print name and age


# 3. Escape Sequences
qestion = "Hello! How are you?"
print(f"He said to me, {qestion}") # Print He said to me, "Hello! How are you?"


# 4. Strings
learning = "I am learning Python"
print(learning)
print(learning[0]) # Print I
print(learning[-1]) # Print n
print(learning[1:6]) # Print 1:6 (from second to fifth letter)


# 5. Strings Methods
learning = " I am learning Python "
print(learning.upper()) # Print in Uppercase
print(learning.strip()) # Print after remove additional spaces


# 6. Strings Formatting
name = "John Doe"
age = 27
print("My name is: %s, and my age is: %d" % (name, age)) # Print the old formatting
print("=" * 20)
name = "John Doe"
age = 27
print(f"My name is: {name}, and my age is: {age}") # Print the new formatting

# 7. Numbers & Arithmetic Operators
a = 10
b = 5

print(a+b) # Addition
print(a-b) # Subtraction
print(a*b) # Multiplication
print(a/b) # Division

# 8. Lists
friends = ["Adam","Cris","Antonio","Mark","Carla"]

print(friends[1]) # Print second name in the list
friends.append("Matt") # Adding a new name to the list
friends.remove("Adam") # Remove first name form list
print(friends) # Print the new list

# 9. Lists Methods
friends = ["Adam","Cris","Antonio","Mark","Carla"]
friends.sort()
print(friends)
friends.reverse()
print(friends)

# 10. Tuples
family = ("Adam","Cris","Antonio")
print(family)
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# 11. Sets
One = {"1","2","3", "4"}
Two = {"4","5","6","7"}
Three = One.union(Two)
print(Three)  # Print union two sets
Four = One.difference(Two)
print(Four)  # Print difference two sets

# 12. Dictionaries
informations = {
    "name": "Jhon Doe",
    "age": "27",
    "city": "London"
}
print(informations) # Print the Dictionary

informations.update({"age": "28"})
print(informations) # Print the Dictionary after update age value

informations.update({"job": "Programmer"})
print(informations) # Print the Dictionary after add new key & Value

# 13. Dictionary Methods
informations = {
    "name": "Jhon Doe",
    "age": "27",
    "city": "London"
}
print(informations) # Print the Dictionary
get_method = informations.get("job", "None") 
print(get_method) # Print the Dictionary with default value
informations.pop("city") 
print(informations) # Print the Dictionary after delete "city" Key

# 14. Comprehensive Training
Todo = []
print(Todo)
Todo.append("Working")
Todo.append("Sleep")
Todo.append("Workout")
Todo.append("Shopping")
Todo.append("Travel")
print(Todo)
Todo.remove("Working")
print(Todo)
Todo[2] = "Study"
print(Todo)
