# Data types
number = 100  # int
second = 57.5  # float
three = "Hello there"  # string
interesting = True  # Bool

# storing multiple vales in a variable
cars = ['Toyota, Nissan, BMW']  # list
fruits = ["Bananas, Apples, Oranges"]  # tuple
countries = {"Kenya, Uganda, Tanzania"}  # set

# Dictionary storing
details = {
 "firstname": "John",
 "Age": 22,
 "Nationality": "Kenyan",
 "Course":  "Health Systems Management"
}

print(number)
print(second)
print(three)
print(cars)
print(fruits)
print(countries)
print(details)
print(details["firstname"])
print(details["Age"])
print(details["Course"])
print(details["Nationality"])

# Determining data types
print(type(details))
print(type(countries))
print(type(fruits))
print(type(number))
print(type(second))
print(type(three))
print(type(cars))

# Typecasting - converting one data type to another
# Explicit
number = float(number)  # converting int to float
print(type(number))
print(number)
number = bool(number)  # converting float to bool
print(number)
print(type(number))
cars = str(cars)  # converting list to string
print(cars)
print(type(cars))
