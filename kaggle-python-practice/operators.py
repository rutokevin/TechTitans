# a + b -> addition sum of a+b (addition operator)
# a - b -> subtraction difference of a and b (subtraction operator)
# a * b -> Multiplication product of a and b (asterisk)
# a / b -> True Division  Quotient of a nad b 
# a // b -> Floor divition Quotient of a and b without decimal part ( int)
# a % b -> Modulus integer remainder after divition
# a ** b -> Exponent a raised to power of b
# -a -> Negation The negative of a

# examles / gives a float
print(5 / 2) #2.5
print(6 / 2 ) #3.0

# // gives an int
print(5 // 2) #2
print(6 // 2 ) #3

# Order of operators
# PEMDAS
# P,E -> Parenthesis,Exponents
# M/D, A/S->Multiplication/Division, Addtion/Subtraction

# e.g 1
print(8 - 3 + 2 ) #7
print(-3 + 4 * 2) #5

#e.g 2
hat_height_cm = 25
my_height_cm = 190

total_height_meters=(hat_height_cm + my_height_cm) / 100
print("Height in Meters = ",total_height_meters, "?")

#better way of printing the above
# f"" -> fstring formatter is used to concatinate strings and variables
print(f"Height in Meters = {total_height_meters} ?")


# build in functions to return minimum, maximam of their arguments
print(min(1,2,3,5)) #returns min -> 1
print(max(1,2,3,7)) #returns max -> 7

# abs returns the absolute of a number
print(abs(10)) # -> 10
print(abs(-10)) # -> 10

#int(), float() -> converts arguments to their types including string numbers e.g "3"
print(float(10)) # -> 10.0
print(int(3.33)) # -> 3

print(int("807") + 1) # -> 807