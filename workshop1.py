import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt

class Equation:
    '''Equation object, it holds the equation, and it's high and low points
    '''
    def __init__(self, equation, low, high):
        self.equation = equation 
        self.low = low
        self.high = high

n = 100  # Number of constants to find
length = np.pi  # Length of the rod
constants = np.zeros(n)  # Holds the constants that we output
equations = [Equation("(20 - ((10*x)/(np.pi/2)))", np.pi/2, np.pi), Equation("(10*x)/(np.pi/2)", 0, np.pi/2)]


# Create constants for all equations
for equation in equations:
    for i in range(1, n+1):
        function = eval("lambda x: " + equation.equation + " * np.sin((i * np.pi * x) / length)")  # Function to integrate
        area,  error  = scipy.integrate.quad(function, equation.low, equation.high)  # Integrate it
        constants[i-1] += (area * (1/length) * 2)  # Add the constants after transforming them by the 2 and 1/length

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