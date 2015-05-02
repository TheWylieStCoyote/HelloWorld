

# This is a simple program to make a plot of random numbers
import numpy as np
import matplotlib.pyplot as plt


def main():
    numbers = np.random.random(100)
    plt.plot(numbers)
    plt.show()

if __name__ == "__main__":
    main()
 