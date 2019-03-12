import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import time

class Equation:
    '''Equation object, it holds the equation, and it's high and low points
    '''
    def __init__(self, equation, low, high):
        self.equation = equation 
        self.low = low
        self.high = high

n = 250  # Number of constants to find
length = np.pi  # Length of the rod
maxTime = 10  # How long to simulate
constants = np.zeros(n)  # Holds the constants that we output
equations = [Equation("5", 0, np.pi/4), Equation("10", np.pi/4, np.pi/2), Equation("0", np.pi/2, 3*np.pi/4), Equation("5", 3*np.pi/4, np.pi)]

#plt.ion()
#fig = plt.figure()
#ax = fig.add_subplot(111)

# Create constants for all equations
for equation in equations:
    for i in range(0, n):

        if i is 0:
            function = eval("lambda x: " + equation.equation) # Function to integrate            
            area,  error  = scipy.integrate.quad(function, equation.low, equation.high)  # Integrate it
            constants[i] += (area * (1/length))  # Add the constants after transforming them by the 2 and 1/length
        else:
            function = eval("lambda x: " + equation.equation + " * np.cos((i * np.pi * x) / length)")  # Function to integrate  
            area,  error  = scipy.integrate.quad(function, equation.low, equation.high)  # Integrate it
            constants[i] += (area * (1/length) * 2)  # Add the constants after transforming them by the 2 and 1/length

# Arrays used to hold the xy pairs
xValues = np.arange(0, length, 0.1)
yValues = np.zeros(xValues.size)  # Initialize this to zero

# Create the xy pairs
for yIndex, x in enumerate(xValues):
    for xIndex, constant in enumerate(constants, 0):
        yValues[yIndex] += (constant * np.cos((xIndex * np.pi * x) / length))  # Get the sum of sines

# Plot and show
#line1, = ax.plot(xValues, yValues, 'b-')

plt.plot(xValues, yValues)
plt.show()


t = 1
while t <= maxTime:
    for yIndex, y in enumerate(yValues):
        yValues[yIndex] = y * np.power(np.e, ((-np.pi * np.pi * y * y * t)/(length*length)))

    #line1.set_ydata(yValues)
    #fig.canvas.draw()
    plt.plot(xValues, yValues)
    plt.show()
    time.sleep(0.5)
    t += 1

# Print the constants for the user
print(constants)