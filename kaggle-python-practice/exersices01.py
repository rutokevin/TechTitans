#favourite color

# create a variable called color and assign it appropriate value
# strings in python must be enclosed in "double" or 'single' quotes

# ex  1 favourite color
color="darkmode"

print(color) # -> darkmode

# ex 2 area of a circle
pi=3.14159 #approximate
diameter=3

# create a valuable called radius equal to half of diameter
radius=diameter / 2

# create a variable area using formula area=Pi*r*r / area=pi*r**2
area =( pi * (radius * radius))

print(area) # -> 7.0685775  

#ex 3 swapping variables
a=[1,2,3] # a list
b=[3,2,1]

print(f"Before swap {a} {b}") # -> Before swap [1, 2, 3] [3, 2, 1]
#swap values to which a and b refer
temp = a # add a third variable to help swap
a = b
b = temp

print(f"After swap {a} {b}") # -> After swap [3, 2, 1] [1, 2, 3]

#easier and short way do swap using tupples
swap=a,b=a,b
print(swap) # ->([3, 2, 1], [1, 2, 3])

#ex 3a evaluate
print(5 - 3 // 2) #-> 4

#ex 3b evaluate and add parenthesis to result to 0
print(((8-3 * 2)-(1 + 1))) #-> 0
#(8-3 * 2)->2
#(1 + 1)->2
#2-2 -> 0

#ex 4 total candies smashed 
#variables rep the number of candies collected by each
alice_candies = 121
bob_candies = 77
carol_candies = 109

#total_smashed_candies is gotten after they split total number of candies collected, equally and smash the remainder
#modulus % operator is used to get remainder
total_smashed_candies = ((alice_candies + bob_candies + carol_candies) % 3)
print(total_smashed_candies) # -> 1