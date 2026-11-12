# EDA: exploratory data analysis
# getting familiar with your data

# we are going to learn how to visualize data w/matplotlib
# 3 goals of data visualization
# 1. clearly and accurately represent data
# 2. be creative, with the goal of increasing understanding
# 3. label units and points of interest

import numpy as np
import matplotlib.pyplot as plt

def plot_data(x, y):
    # let's have 2 charts in one "figure"
    # the 2 charts will be side by side in one row
    fig, axes = plt.subplots(1, 2, figsize=(12, 4)) # 12" width x 4" height


    fig.tight_layout() # good to call last, after adding all figure components

def main():
    # we need some data!
    x = np.arange(10) # 0 1 2 ... 9
    y = np.random.randint(1, 101, len(x)) # random ints in [1, 101)
    print(x)
    print(y)

    # 1st demo: using the pyplot interface (simplest)
    # plt.plot(x, y)
    # plt.show() # shows an interactive window

    # 2nd demo: using the "object oriented" interface (more control)
    plot_data(x, y)
    plt.savefig("demo.png") # instead of showing window, let's save figure to a file

main()