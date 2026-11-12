# EDA: exploratory data analysis
# getting familiar with your data

# example of EDA: data visualization
# goals of data viz
# 1. clearly and accurately represent data
# 2. be creative, with the goal of increasing understanding
# 3. label units and points of interest

import numpy as np
import matplotlib.pyplot as plt

def plot_data(x, y):
    # let's have one figure with 2 charts in a row
    fig, axes = plt.subplots(1, 2, figsize=(12, 4)) # 12" width x 4" height


    # after add all chart components good to call:
    fig.tight_layout()

def main():
    # 1st demo: using the pyplot interface (simplest)
    # we need data
    x = np.arange(10) # 0 1 2 3... 9
    y = np.random.randint(1, 101, len(x)) # [1, 101)
    # print(x)
    # print(y)
    # plt.plot(x, y)
    # plt.show() # launches an interactive window

    # 2nd demo: using "object oriented" interface (more control)
    plot_data(x, y)
    plt.savefig("demo.png")

main()