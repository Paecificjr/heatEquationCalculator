import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

n = 10  # Number of constants to find
length = np.pi  # Length of the rod
constants = []  # Holds the constants that we output
equation = "(20 - ((10*x)/(np.pi/2)))"  # Function to find solution for
low = np.pi/2
high = np.pi
#equation = "(10*x)/(np.pi/2)"
#low = 0  # Lower bound
#high = np.pi/2  # Upper bound

# Create constants
for i in range(1, n+1):
    function = eval("lambda x: " + equation + " * np.sin((i * np.pi * x) / length)")  # Function to integrate
    area,  error  = scipy.integrate.quad(function, low, high)  # Integrate it
    constants.append(area * (1/length) * 2)  # Add the constants after transforming them by the 2 and 1/length

# Arrays used to hold the xy pairs
xValues = np.arange(0, length, 0.1)
yValues = np.zeros(xValues.size)  # Initialize this to zero

# Create the xy pairs
for yIndex, x in enumerate(xValues):
    for xIndex, constant in enumerate(constants, 1):
        yValues[yIndex] += (constant * np.sin((xIndex * np.pi * x) / length))  # Get the sum of sines

# Plot and show
plt.plot(xValues, yValues)
plt.show()

# Print the constants for the user
print(constants)