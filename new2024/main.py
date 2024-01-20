# importing numpy module
import numpy as np

#populating arrays with numbers

one_dimensional_array = np.array([1.2, 2.4, 3.5, 4.7, 6.1, 7.2, 8.3, 9.5])
print(one_dimensional_array)

two_dimensional_array = np.array([[6, 5], [11, 7], [4, 8]])
print(two_dimensional_array)

#populate array with sequence of numbers

sequence_of_integers = np.arange(5, 12)
print(sequence_of_integers)

#populating arrays with random numbers
random_integers_between_50_and_100 = np.random.randint(low=50, high=101, size=(6))
print(random_integers_between_50_and_100)

#To create random floating-point values between 0.0 and 1.0

random_floats_between_0_and_1 = np.random.random([6])
print(random_floats_between_0_and_1)

#broadcasting

random_floats_between_2_and_3 = random_floats_between_0_and_1 + 2.0
print(random_floats_between_2_and_3)

random_integers_between_150_and_300 = random_integers_between_50_and_100 * 3
print(random_integers_between_150_and_300)

'''
Your goal is to create a simple dataset consisting of a single feature and a label as follows:
Assign a sequence of integers from 6 to 20 (inclusive) to a NumPy array named feature.
Assign 15 values to a NumPy array named label such that:label = (3)(feature) + 4 =22'''

feature = np.arange(6 ,21)
print(feature)
label = (3*feature)+ 4
print(label)

''' '''
noise = (np.random.random([15]) * 4) - 2
print(noise)
label = label + noise
print(label)